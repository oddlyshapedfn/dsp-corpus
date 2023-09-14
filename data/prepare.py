import json
import pandas as pd
import re

import os
import sys
from bs4 import BeautifulSoup

def make_record(text, author, source):
    return {
        "text": "<dsp-llm>: {}<|endoftext|>".format(text),
        "metadata": {"source": source, "author": author}
    }

def prepare_koh():
    basedir = './raw/koh_forum_posts/'
    savepath = './prepared/'
    files = os.listdir(basedir)
    for x in files:
        fname = os.path.join(basedir, x)
        cm_clean = None
        with open(fname, 'r', encoding='utf-8') as fp:
            soup = BeautifulSoup(fp, features='html.parser')

            # First, drop all quote blocks.
            for quote in soup.find_all('blockquote'):
                quote.extract()

            # Find comment blocks. Comments might have a nested quote block that needs
            # to be dropped
            comments = soup.find_all(re.compile('^div$'), attrs={"data-role": "commentContent"})
            cm_clean = [str(x.p.string).strip() for x in comments if x.p is not None]
            print(cm_clean)

        savename = os.path.basename(fname)
        savename = os.path.join(savepath, savename) + '.jsonl'
        with open(savename, 'w', encoding='utf-8') as f:
            jsonres = []
            for value in cm_clean:
                entry = make_record(value, 'Phil', 'KOH Forum')
                f.write("{}\n".format(json.dumps(entry)))

def prepare_twitter():
    tbl = pd.read_csv('raw/twitter/dsp-tweet-archive-2020.csv')

    with open('prepared/dsptwitter.jsonl', 'w', encoding='utf-8') as f:
        for tw in tbl['tweet'][::40]:
            # Try to delete anything that looks like a URL
            text = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", tw)

            # Delete or replace unicode characters that twitter uses for newlines and '
            text = text.replace(chr(0x2019), "'")
            text = text.replace(chr(0x00a0), "")
            text = text.replace(chr(0x2026), "")

            # Remove leading and trailing whitespace
            text = text.strip()

            # Remove a stack of blip.tv repost tweets
            if 'to blip.tv' in text:
                continue
            entry = make_record(text, "dspgaming", "twitter")
            f.write("{}\n".format(json.dumps(entry)))

# Some irregularities in the data:
# * Sometimes lines continue on a new line with the [xx:yy] <user> tag, sometimes
#   the tag does appear.
# * Usually a full message ends with a newline, but there some to be some exceptions when
#   it's the same author consecutively.
# * There are some system messages (Sesson, sg-param, ...) that need to be filtered
# * There are some inline comments from the person who collected the data.
# * When someone subscribes, there's a message with a timestamp but no author.
class TwitchEddyB43Parser:
    def __init__(self, base_dir, ignore_keys=None):
        self.base_dir = base_dir
        self.fnames = None
        self.ignore_keys = [
            "Session",
            "sg-param-sub-plan",
            "[mod",
            "just subscribed with",
            "Manually split"
        ]
        if ignore_keys:
            self.ignore_keys += ignore_keys

    def check_valid_line(self, text):
        for key in self.ignore_keys:
            if key in text:
                return False;

        return True

    def parse_one(self, fname):
        res = []
        last_name = ""
        with open(fname, 'r', encoding='utf-8') as f:
            for line in f:
                if not self.check_valid_line(line):
                    continue
                sep = re.findall("<.*>", line)
                if sep == []:
                    if not line.strip():
                        # Empty line!
                        last_name = ""
                        res.append(("newline", last_name, ""))
                    else:
                        # Continued Text w/o name
                        res.append(("accumulate", last_name, line))
                else:
                    (ts, name, msg) = line.partition(sep[0])
                    # Same name, extend previous message
                    if not name or not msg:
                        continue
                    elif name == last_name:
                        res.append(("accumulate", last_name, msg))
                    # Different name
                    else:
                        last_name = name
                        res.append(("newmsg", last_name, msg))
        # Simple state machine to merge adjacent entries.
        merged = []
        running_entry = ""
        for action, nm, value in res:
            x = nm
            if action == "newline":
                running_entry.replace('\n', ' ')
                merged.append((last_name, running_entry))
            elif action == "newmsg":
                running_entry = value.strip()
                last_name = nm
            elif action == "accumulate":
                running_entry += value.strip()

        ret = []
        for author, text in merged:
            ret.append(
                make_record(text, author.strip('<>'), "twitch")
            )
        return ret

def prepare_manual(fname, source_name = "manual", author="DSP", unsure=True, savepath='./prepared'):
    res = []
    with open(fname, 'r', encoding='utf-8') as f:
        msg = ""
        for line in f:
            if line.startswith("##"):
                res.append(msg)
                msg = ""
                continue
            if line.startswith('>'):
                continue

            msg = msg.replace(chr(0x2019), "'")
            msg = msg.replace(chr(0x00a0), "")
            msg = msg.replace(chr(0x2026), "")
            msg += line.replace('\n', ' ')

    savename = os.path.basename(fname)
    savename = os.path.join(savepath, savename) + '.jsonl'
    with open(savename, 'w', encoding='utf-8') as f:
        jsonres = []
        for value in res[1:]:
            if ("&& UNSURE" in value) and not unsure:
                continue
            value = value.replace('&& UNSURE', '')

            # Split approximately by sentences
            # for line in value.split('.'):
                # if len(line) < 5:
                    # continue
            entry = make_record(value.strip(), author, source_name)
            jsonres.append(entry)
            f.write("{}\n".format(json.dumps(entry)))

    return jsonres

if __name__ == '__main__':
    if False:
        prepare_twitter()

    if True:
        prepare_koh()

    if False:
        parser = TwitchEddyB43Parser('raw/twitch/all_chat')
        parser.parse_dir()

    if True:
        x = prepare_manual(
            'raw/srk_archive/eccxi.txt',
            source_name="SRK",
            author="DarksydePhil"
        )
        x = prepare_manual(
            'raw/srk_archive/blaze_asks_em.txt',
            source_name="SRK",
            author="DarksydePhil"
        )
        x = prepare_manual(
            'raw/srk_archive/ct_thread.txt',
            source_name="SRK",
            author="DarksydePhil"
        )
        x = prepare_manual(
            'raw/srk_archive/evo_console_controversy.txt',
            source_name="SRK",
            author="DarksydePhil"
        )
        x = prepare_manual(
            'raw/srk_archive/misc.txt',
            source_name="SRK",
            author="DarksydePhil, Punish3r, dXp"
        )
        x = prepare_manual(
            'raw/srk_archive/mwc_results_627.txt',
            source_name="SRK",
            author="Punish3r"
        )
        x = prepare_manual(
            'raw/srk_archive/new_female_thread.txt',
            source_name="SRK",
            author="Punish3r"
        )
        x = prepare_manual(
            'raw/srk_archive/use_of_consoles_evo2k4.txt',
            source_name="SRK",
            author="DarksydePhil"
        )
        x = prepare_manual(
            'raw/srk_archive/wc_vs_ec.txt',
            source_name="SRK",
            author="Punish3r"
        )
        x = prepare_manual(
            'raw/sf2_ggroup/alt_games_sf2.txt',
            source_name="SF2 Google group",
            author="WhoaMoses, Darksyde"
            )
        x = prepare_manual(
            'raw/manual/screenshots.txt',
            source_name="Discord",
            author="TheyCallMeDSP"
        )

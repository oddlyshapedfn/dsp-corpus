# DSP Corpus
Text dataset of DSP ramblings

# Usage
```
cd data
python prepare.py
```

# Data sources
## Raw
Raw data sources, unparsed or lightly parsed. Data preparation scripts will transform these into
the format training scripts need. Specifically, we'll try to follow the schema [OIG](https://huggingface.co/datasets/laion/OIG)
uses, jsonl.
```
{"text": "<human>: Hi!\n<bot>: Hi! How can I assist you today?", "metadata": {"source": "basic"}}
{"text": "<human>: Hi there!\n<bot>: Hello! How can I assist you today?", "metadata": {"source": "basic"}}
{"text": "<human>: Hey!\n<bot>: Hi there! How can I help you?", "metadata": {"source": "basic"}}
{"text": "<human>: Greetings!\n<bot>: Hello! How may I be of assistance?", "metadata": {"source": "basic"}}
```

## Not included
This dataset should only contain written text, and not transcribed speech.

### KOH forum
73 pages worth of posts from the KOH forums.
All links have had the leading portion of the URL replaced so they can't be
clicked unintentionally. This means that images will also not load.
Notes:
* This dataset contains many short and redundant messages from his Ask the king announcement posts.

### SF2 Google Group
Posts by WoahMoses, DarkSyde, and another Deja address that appears to be him.

### Other Google Group
See https://www.youtube.com/watch?v=EiuQ_eo-b7U

### Twitter
Posts by DSP on twitter. Since API access is no longer free, recent tweets
are not available.
* https://archive.org/details/dsp-tweet-archive-2020 by Egdon Bitervin

### Twitch
Chat logs archived by EddyB43 on archive.org. Mostly covers 2017/2018
While some of the archive is preprocessed to only have DSP's messages, some
include ALL chat messages and must be filtered by looking for messages by
`<darksydephil>`. Additionally, multiline messages must be merged manually,
but you can tell when a single long message  ends because a newline occurs.
* https://archive.org/search?query=creator%3A%22EddyB43%22

### SRK forum archive
This is really tedious to archive. FYI: the forum runs on [Flarum](https://github.com/flarum/flarum), so perahps
a scraper for this SW exists.
* https://pypi.org/project/pyFlarum/

### top-haters.com
Coming eventually. See notes in the `missing` section.

Known aliases:
`darksydephil`
`punish3r`
`dXp`

DONE:
* (DarksydePhil) https://archive.supercombo.gg/t/eccxi-the-saga-continues-8-on-the-break-arcade-may-26-2006-may-29-2006/15662
* (DarksydePhil) https://archive.supercombo.gg/t/the-ct-thread/1844/556
* (Punish3r) https://archive.supercombo.gg/t/fallout-in-ct-results-7-26/1975
* (Punish3r) https://archive.supercombo.gg/t/new-female-thread/13/15
* (dXp) https://archive.supercombo.gg/t/my-roommate-infinite-vs-team-trash-florida/27891/44 (contains posts by Mixup?)
* (DarksydePhil) https://archive.supercombo.gg/t/evo-console-controversy-solved/5108/38
* (DarksydePhil) https://archive.supercombo.gg/t/the-new-boston-thread-revived/4500/48
* (DarksydePhil) https://archive.supercombo.gg/t/final-round-7-saturday-results/5368/165
* (DarksydePhil) https://archive.supercombo.gg/t/shintea-time-results-4-3-04/5247/5
* (DarksydePhil) https://archive.supercombo.gg/t/use-of-consoles-at-evo2k4/5065/127
* (DarksydePhil) https://archive.supercombo.gg/t/blaze-asks-em-why-srk-died-and-how-it-was-reborn/5535/7
* (DarksydePhil) https://archive.supercombo.gg/t/5-20-mvc2-the-break-results/6028/11 (funny)
* (DarksydePhil) https://archive.supercombo.gg/t/break-deodorant-5-2-2004-org-comes-out-on-top/5738/9
* (DarksydePhil) https://archive.supercombo.gg/t/play-us-5-guys-for-money-mvc2/5448/3
* (DarksydePhil) https://archive.supercombo.gg/t/which-players-do-you-all-think-should-be-on-team-ec-wc-in-mvc2-this-year-at-evo2k4/5208/26
* (DarksydePhil) https://archive.supercombo.gg/t/money-bets-vs-chobazzle-ggxx-mvc2/5052/31
* (DarksydePhil) https://archive.supercombo.gg/t/ncr2-sun-results/5270/193
* (DarksydePhil) https://archive.supercombo.gg/t/official-grudge-match-thread/5079/21 (Maybe the start of the MM with mixup?)
* (DarksydePhil) https://archive.supercombo.gg/t/open-challenge/5202/8
* (DarksydePhil) https://archive.supercombo.gg/t/breakdown3-feb-28-29-2004/4696/57
* (Punish3r) https://archive.supercombo.gg/t/evolution2k3-updates-results-upsets-etc/2084/11
* (Punish3r) https://archive.supercombo.gg/t/wc-vs-ec-5-on-5/1887/155 (Flamewar with mixup)
* (Punish3r) https://archive.supercombo.gg/t/official-mwc-results-day-1-6-27-omaha-ne-family-fun-center/1740/106 (funny)
* (Punish3r) https://archive.supercombo.gg/t/ghetto-results-from-atl-south-justinw-xecutioner-pre-evolution-tourney-07-05-03/1793/6
* (Punish3r) https://archive.supercombo.gg/t/what-is-the-stick-situation-going-to-be-at-evo-360-8-way/1563/27
* (Punish3r) https://archive.supercombo.gg/t/glendales-bitch-vs-soo-round-2/1654/13
* (Punish3r) https://archive.supercombo.gg/t/official-ecc8-results/1556/49
* (Punish3r) https://archive.supercombo.gg/t/6-5-8otb-results-bets/1651/6
* (Punish3r) https://archive.supercombo.gg/t/meeting-soomighty-rowtron-and-jusin-wong/1609/16
* (Punish3r) https://archive.supercombo.gg/t/ecc-shreks-report/1562
* (Punish3r) https://archive.supercombo.gg/t/sentinel-unblockable-banned/1481/94
* (Punish3r) https://archive.supercombo.gg/t/ecc8-mvc2-results/1546/54
* (Punish3r) https://archive.supercombo.gg/t/ecc-st-results/1523/25
* (Punish3r) https://archive.supercombo.gg/t/5-1-mvc2-at-the-break-results/1359/4
* (Punish3r) https://archive.supercombo.gg/t/rules-question/1372/6
* (Punish3r) https://archive.supercombo.gg/t/the-break-mvc2-st-results-4-17-03/1244/6
* (Punish3r) https://archive.supercombo.gg/t/chaos-in-ct-results-jesters-arcade-capcom-vs-snk-2-3-28-03/1111/3
* (Punish3r)

TODO:
* https://archive.supercombo.gg/t/jesters-waterford-ct-weekly-mvc2-cvs2-2-21/812/11
* https://archive.supercombo.gg/t/north-east-championship-nec3-results-thread/448/12
* https://archive.supercombo.gg/t/jersey-break-down-11-10-02-with-pics-and-videos-really-theyre-up/373/27
* https://archive.supercombo.gg/t/mvc2-break-results-for-nov-10th-jersey-break-down/368/12
* https://archive.supercombo.gg/t/cvs2-character-cloning/591/26
* https://archive.supercombo.gg/t/the-official-custom-arcade-sticks-thread/504/1384
* https://archive.supercombo.gg/t/tokyo-game-action-presents-tga-ranking-battle-results-8-12-06/17982/12
* https://archive.supercombo.gg/t/total-barnage-official-results/1444/11

dXp:
* https://archive.supercombo.gg/t/showdown-championships-results/24183/11
* https://archive.supercombo.gg/t/showdown-championships-apr-27-29-houston-tx/21160/91
* https://archive.supercombo.gg/t/tokyo-game-action-presents-usa-ec-tougeki-sbo-qualifiers-june-9-10-16-17/21632/11
* https://archive.supercombo.gg/t/my-roommate-infinite-vs-team-trash-florida/27891/9
* https://archive.supercombo.gg/t/we-need-more-st-players-in-seattle/23941/535
* https://archive.supercombo.gg/t/team-hate-cave/11359/1031
* https://archive.supercombo.gg/t/more-new-videos-from-evo-east-st-and-ssbm-updated-06-27-2007/25778/11
* https://archive.supercombo.gg/t/slammin-saturday-nights-the-revenge-at-web2zone-july-14th/25316
* https://archive.supercombo.gg/t/evo-north-the-midwest-championships-thread/18280/62
* https://archive.supercombo.gg/t/planet-zero-houston-presents-dr-ggac-arcana-heart-sc3-2007-sbo-qualifiers/24545/31
* https://archive.supercombo.gg/t/accent-core-at-evo-you-can-make-it-happen/23987/34
* https://archive.supercombo.gg/t/evo-east-the-east-coast-championships-may-25-27-2007/22499/13
* https://archive.supercombo.gg/t/intro-music/22636/13
* https://archive.supercombo.gg/t/min-masters-presents-super-practice-opera-web2zone-may-19/24188/19
* https://archive.supercombo.gg/t/i-challenge-mike-chaos-evo/23105/11
* https://archive.supercombo.gg/t/dark-prince-aka-duc-jr-is-officially-banned-from-the-evo-series/24041/118
* https://archive.supercombo.gg/t/ssf2turbo-xbox360-capcom-gamers-day-rumor/23533/24
* https://archive.supercombo.gg/t/4-1-3s-buy-com-lan-2007-in-anaheim-ca/23151/78
* https://archive.supercombo.gg/t/nelson-aka-remix-is-toxic-vs-harry-potter-300-money-match/25453/25
* https://archive.supercombo.gg/t/new-ct-thread/26286/8
* https://archive.supercombo.gg/t/beneath-the-streets-tmnt-tournament-fighters-snes-evo/22973/6
* https://archive.supercombo.gg/t/ecc-12-5-dunellen-nj-10-6-07-10-7-07/26987/78
* https://archive.supercombo.gg/t/i-just-got-back-from-gvr-for-the-weekend-some-helpful-shit-for-evo/27848/11
* https://archive.supercombo.gg/t/evo-world-welcome-to-green-valley-ranch-schedule-live/26132/6
* https://archive.supercombo.gg/t/the-official-evo-world-training-preparation-video/27939/15
* https://archive.supercombo.gg/t/gg-ac-ps2-version-evo-worlds/26640/35
* https://archive.supercombo.gg/t/ctf-week-before-evolution/27760/12
* https://archive.supercombo.gg/t/team-florida-shits-on-phil-challenge-will-he-accept/27949/18
* https://archive.supercombo.gg/t/evo-world-special-event-2-east-coast-vs-west-coast-5on5-mvc2-rematch/27449/8
* https://archive.supercombo.gg/t/ffa-sbo-west-coast-usa-qualifiers-ae-results/24593/21
* https://archive.supercombo.gg/t/street-fighter-ii-turbo-hyper-fighting/27000/8
* https://archive.supercombo.gg/t/dipset-pigadoken-evo-world-mm-thread/22211/91
* https://archive.supercombo.gg/t/me-vs-rina-morse-first-to-10-for-100-at-evo-world-please-lock/26114/28
* https://archive.supercombo.gg/t/marvel-matches-that-should-take-placeeee/27066/20
* https://archive.supercombo.gg/t/tokyo-game-action-presents-sbo-east-coast-qualifier-updated-results/25669/14
* https://archive.supercombo.gg/t/evo-west-west-coast-championships-registration-live/24750/113
* https://archive.supercombo.gg/t/happy-b-day-to-oldman-edpachi/26614/16
* https://archive.supercombo.gg/t/poll-who-wants-to-see-a-mm-worth-est-10-000-bucks-in-3s-at-evo-world/26192/40
* https://archive.supercombo.gg/t/evo-south-america-for-2008/22086/30
* https://archive.supercombo.gg/t/evo-north-i-want-to-split-a-room-at-red-roof-thread/25921/3
* https://archive.supercombo.gg/t/planet-zeros-sbo-qualifier-history/25450/15
* https://archive.supercombo.gg/t/blaze-vs-matrix-evo-teams-retirement-match/25216/23
* https://archive.supercombo.gg/t/samir-the-cheater/25145/104
* https://archive.supercombo.gg/t/should-one-button-dash-in-mvc2-be-banned-from-evo/24937/36
* https://archive.supercombo.gg/t/the-official-hsien-chang-vs-any-ffa-chump-mm-thread/24900/17
* https://archive.supercombo.gg/t/evo-regional-qualifier-spots-question/24911/7
* https://archive.supercombo.gg/t/the-return-of-slammin-saturday-nights-web2zone-4-28-results/24104/5
* https://archive.supercombo.gg/t/dark-prince-vs-shady-k-videos/23624/7
* https://archive.supercombo.gg/t/4-14-c3-results/23608/47
* https://archive.supercombo.gg/t/cal-poly-pomona-tourney-live-results/23102/42
* https://archive.supercombo.gg/t/evo-east-gathering-with-fist-of-the-north-star/23012/6
* https://archive.supercombo.gg/t/eder-the-cheder-vs-vegita-x-ft10-500/23588/15
* https://archive.supercombo.gg/t/mike-chaos-vs-yipes-and-wigfall-will-he-back-up-his-mouth/23413/31
* https://archive.supercombo.gg/t/evo-east-question/23273/4
* https://archive.supercombo.gg/t/byoc-single-player-game-mms/22790/8
* https://archive.supercombo.gg/t/breakdown-6-results/22041/12
* https://archive.supercombo.gg/t/the-going-away-tourny-at-chinatown-fair-3-17-07/22178/11
* https://archive.supercombo.gg/t/wc-mvc2-teams-made-by-you-cast-your-vote/21383/197
* https://archive.supercombo.gg/t/the-official-evo-south-roster-thread/22349/5
* https://archive.supercombo.gg/t/bunkei-invites-duc-jr-mike-chaos-to-alphaism-radio/22097/30
* https://archive.supercombo.gg/t/breakdown-6-spit-it-saturday-feb-24-2007/21156/12
* https://archive.supercombo.gg/t/nyclan-heartbreaker-express/20440/101
* https://archive.supercombo.gg/t/cf-mvc2-new-blood-results-1-20-07/21029/22
* https://archive.supercombo.gg/t/cf-mvc2-new-blood-tourney-1-20-07/20779/18
* https://archive.supercombo.gg/t/tga-tournament-results-for-3s/20652/37

### Manual
Any text from sources that must be entered manually, such as in images.

### Missing
* Probably a bunch of stuff from the SRK links. It's not always obvious which one is him.
* Anything from the champions Discord. Probably inaccessible by this point, might be
  archived on KF. Some screencaps from various twitter users that need to be transcribed
* Mod Discord leak. Only have videos of others reading the KF thread, so some stuff probably missing
* `top-haters.com`. It's [archived](https://web.archive.org/web/20041009164646/http://www.top-haters.com/main.htm) by waybackmachine, so it shouldn't be hard to copy it later.

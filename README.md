<h1 align="center">Insta Stats</h1>

<p align="center">
  <b>Display your Instagram statistics.</b>
</p>

[![Maintainability](https://img.shields.io/codeclimate/maintainability/alexlostorto/insta-stats?style=for-the-badge&message=Code+Climate&labelColor=222222&logo=Code+Climate&logoColor=FFFFFF)](https://codeclimate.com/github/alexlostorto/insta-stats/maintainability)

The program automatically retrieves the user's Instagram statistics using **Instagram's GraphQL API**.

```python
# Examples in console
╭─────────────────────────────────────────────────────────────────────────╮
│                               Followings                                │  
├──────────────────────────┬──────────────────────────────────────────────┤  
│         Username         │                   Full Name                  │  
├──────────────────────────┼──────────────────────────────────────────────┤  
│         jordancs1        │                Jordan Shepherd               │  
│         zephybite        │                 angela he 💫😈              │
│       gathersocial       │                 Gather Social                │  
│      liveregularttv      │                     Peter                    │  
│       neo_nski.xero      │                   Daniel O                   │  
│       a.alquintojr       │                Thoto Alquinto                │
│         badq.png         │                                              │
│       weareparaiso       │                    PARAISO                   │
│        muqeet_295        │                 Abdul Muqeet                 │
...

+──────────────────────────────────────────────────────────────────────────+
│                                Followers                                 │
+────────────────────────────────+─────────────────────────────────────────+
│            Username            │               Full Name                 │
+────────────────────────────────+─────────────────────────────────────────+
│         easydrawingusa         │             Easy drawing                │
│            gkirschel           │             Giv Kirschel                │
│          __sami.arts__         │              Samila Mak                 │
│       poiotikh_zwgrafikh       │          Fantastic arts 🖌️🎨           │
│      _____brightlight____      │                Samila                   │
│            za.kikiy            │               za. kikiy                 │
│           hawking_43           │              Zahid Azkaa                │
│         mandafilia.a.s         │                                         │
│       folowakun_yangdibio      │                                         │
│             ofie133            │                 ofie                    │
│          saadatikamila         │             Petis Mercon                │
│      sapphire_and_isabella     │         Sapphire and Isabella           │
...
```

## ⚡ Quick setup

1. Clone the repo

```bash
git clone https://github.com/alexlostorto/insta-stats
```

2. Rename _.env.example_ to _.env_

3. Replace the _username_ with any **Instagram username** and replace _cookie_ with the Instagram **cookies** when you are logged in.

```env
USER=username
COOKIE=cookie
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run main.py

```bash
python main.py
```

6. Star the repo 😄

## 📜 Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.

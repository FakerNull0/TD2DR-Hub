import re

RAW_TEXT = """
https://gamejolt.com/games/lisitsynfox/1054471 - v1101 PC / Android (TD2DR Curse of Chaos) by Lisitsyn
https://github.com/AX88M2/DisasterServer - v1101 - v1012 - v100 - v206 (исходные коды сервера в одном в разных ветках) by MilesGlitch
https://github.com/thearcticfox25/AdvancedServer/ - v1101 (модифицированный сервер) by The Arctic Fox
https://github.com/thearcticfox25/sonic.exe-mp/ - Separate Project PC (Sonic.EXE: Multiplayer) by The Arctic Fox
https://gamejolt.com/games/TD2DRgmcycle/919987 - v1101 (модифицированный сервер) by IceCoffee & ColdestTea
https://gamejolt.com/games/TD2DR_Sonic/919101 - v1101 PC / Android (TD2DR X Sonic) by Renx Diamond
https://gamejolt.com/games/td2drUR/938171 - v1101 PC (TD2DR Universe Relapse) by Relapse Team
https://gamejolt.com/games/Disaster2DRemakeNUProject/1015209 / https://gamebanana.com/mods/589527 - v1101 PC (Sonic.exe The Disaster 2D Remake NU Project) by Remodify Studio
https://gamejolt.com/games/tdr/838670 - Separate Project (Sonic.EXE: The Disaster (2D) Redux) by immails
https://gamejolt.com/games/td2dr_doubletrouble/940798 - v1101 PC / Android (Sonic.exe The Disaster 2D Remake: Double Trouble) by IceCoffee & ColdestTea
https://gamejolt.com/games/td2dTD2DThroughtheblood/1034288 - v1101 PC / Android (Sonic.exe The Disaster 2D Remake Through The Blood) by maxbaxwer
https://gamejolt.com/games/NEXUS/912415 - v1101 PC (Sonic.exe The Disaster 2D Remake Nexus) by sonicstudiox
https://gamejolt.com/games/olr_project_TD2DR/1077062 - v1101 PC / Android (TD2DR One Last Round Project) by ModHive Studio
https://gamejolt.com/games/TD2DR_X_Brandon/1053859 - v1101 PC / Android (Sonic.exe The Disaster 2D Remake X Brandon) by BrandonTheHedgehog
https://gamejolt.com/games/test/866396 - v100 - v1014 / PC / Android (Brandon The hedgehog in Sonic.exe The Disaster 2D Remake) by BrandonTheHedgehog 
https://gamejolt.com/games/SonicExeTD2DRMODIFIED/1020980 - v1101 PC (Sonic.exe The Disaster 2D Remake Modified) by JAYDENDOESTHINGS831
https://gamejolt.com/games/2Dthedisasterclassicgirlsmod/872335 - v1101 PC (TD2DR - Classic Girls Edition) by Pure Platinum Killer (PPK)
https://gamejolt.com/games/TD2DR-RUS/1072577 - v1101 - PC / Android (Sonic.exe The Disaster 2D Remake Руссификатор) by ModHive Studio
https://gamejolt.com/games/fakermod/908703 - v100 - PC (The Disaster 2D Remake ModGen Faker Mod) by DollFan
https://gamejolt.com/games/td2d_skybase/855567 - v1101 - PC / Android (TD2DR: Sky Base Project) by IceCoffee & ColdestTea
https://gamejolt.com/games/sonicfanrus-zycptb/863131 - v100 - PC (Sonic.exe The Disaster 2D Remake - New Friends Forever!) by Alpha_Parallax
https://gamejolt.com/games/td2drrepentcastlemod/894952 - v100 / v1014 - PC(The Disaster 2D Remake Repent Castle Map) by DemonZIDE
https://gamejolt.com/games/td2drbfds/916769 - v100 - PC (The Disaster 2D Remake Bowser's Fortress DS Map) by DemonZIDE
https://gamejolt.com/games/td2drvoidflat/899447 v100 - PC (The Disaster 2D Remake Void Flat Custom Map) by DemonZIDE
https://gamejolt.com/games/td2dr_lostsouls/1040400 - v1101 - PC / Android (Sonic.exe The Disaster 2D Remake: Lost Souls) by sunblizz
https://gamejolt.com/games/remake_by_pupsik228/866954 - v100 (PC) - v1101 PC / Android (TD2DR Stefan joins) by Pupsik228
https://gamejolt.com/games/TD2DR_Project_Shadow/1050440 - v1101 - PC / Android (TD2DR X Shadow) by KAMI-2012
https://gamejolt.com/games/AmelTD2DR/893704 - v100 - v1101 - PC (Amelia in TD2DR) by MORBUN
https://gamejolt.com/games/crimsoneditionbyss/1067267 - v1101 - PC (TD2DR Crimson Edition) by SamuServian
https://gamejolt.com/games/onemorefun/967599 - v1101 - PC (TD2DR One More Fun) by OneLastProductions
https://gamejolt.com/games/TD2DR-SONICS-REVENGE/957458 - v1101 - PC / Android (TD2DR Sonic's Revenge) by Assasin4568 (Ported)
https://gamejolt.com/games/TD2DR-sonic/877606 - v100 - v1014 - PC / Android (TD2DR Sonic's Revenge) by BrandonTheHedgehog (Original)
https://gamejolt.com/games/TD2DR-DEATHMATCH-OF-DESPAIR/996178 - v1101 - PC / Android (TD2DR Deathmatch of Despair) by Assasin4568 (Ported)
https://gamejolt.com/games/TD2DDMoD/895430 - v100 - PC (TD2DR Deathmatch of Despair) by FakerEXE (Original)
https://gamejolt.com/games/Ports-Mania-In-TD2DR-V1101/997230 - v1101 - PC / Android (TD2DR Mania Mod) by Assasin4568 (Ported)
https://gamejolt.com/games/TD2DR-Mania-Mod/897659 - v100 - PC / Android (TD2DR Mana Mod) by BrandonTheHedgehog (Original)
https://gamejolt.com/games/Pc-and-Android-Ports-TD2DRR/995301 - v1101 - PC / Android (The Disaster 2D Revamped) by Assasin4568 (Ported)
https://gamejolt.com/games/td2drr/857034 - v100 - PC (The Disaster 2D Revamped) by Cheizburr (Original)
https://gamejolt.com/games/Ports-td2d-mod-reskin-dimalapt-v1101/937263 - v1101 - PC / Android (TD2DR Dimalapt Reskins Pack) by Assasin4568 (Ported)
https://gamejolt.com/games/td2dDimalaptReskinspack/858979 - v100 - PC / Android (TD2DR Dimalapt Reskins Pack) by Dimalapt (Original)
https://gamejolt.com/games/Project-Sonic-Omt/932308 - v1101 - PC / Android (Project Sonic.OMT) by Assasin4568
https://gamejolt.com/games/IronForesttd2dr/916013 - v1014 - PC (TD2DR Iron Forest over Hide and Seek Act 2) by ANormalGaze
https://gamejolt.com/games/baseformexellertd2dr/916016 - v1014 - PC (TD2DR Normal/Base Form Exeller Mod) by ANormalGaze
https://gamejolt.com/games/fleetwayamytd2dr/916182 - v1014 - PC (TD2DR Fleetway Amy Mod) by ANormalGaze
https://gamejolt.com/games/amyslide/925750 - v1101 - PC (TD2DR but Amy can slide) by X-Fluffy-X
https://gamejolt.com/games/td2dr_friends_of_jimbo/1082189 - v1101 - in development (TD2DR: Friends of Jimbo) by Gasterovi4
https://gamejolt.com/games/wood_zone_lol/865011 - v100 - PC (Wood Zone in TD2DR) by DeklynTDH
https://gamejolt.com/games/td2drlatino/1010516 - v1101 - PC (TD2DR Latino Mod) by DumbDotJpg
https://gamejolt.com/games/snowexe/956813 - v1101 - PC / Android (TD2DR XMAS (Winter Edition) Mod) by X-Fluffy-X
https://gamejolt.com/games/td2draprilfoolsmod/887216 - v100 - PC / Android (TD2DR April Fools) by Hacha
https://gamejolt.com/games/Disaster2DRemakeCOTVPCPORT/895727 - v1014 - PC (TD2DR Call of The Void Port) by ProtagonistReal
https://gamejolt.com/games/CotvAndroid1014/896316 - v1014 - Android (TD2DR Call of The Void Port - based on ProtagonistReal version) by Miles3
https://gamejolt.com/games/sonicexetd2drthedisastrousmultiverse/894259 - v1101 - PC (Sonic.EXE TD2DR: The Disastrous Multiverse) by Lski
https://gamejolt.com/games/TD2DR_Version_2012/1096056 - v1101 - PC / Android (TD2DR v2012) by KAMI-2012
https://gamejolt.com/games/TD2DR-Crushed-Dimension-v1101/1012959 - v1101 - PC (TD2DR Crushed Dimensions) by MaloverD07
https://gamejolt.com/games/TD2DR-But-All-EXES-V1101/1073455 - v1101 - PC (TD2DR but all Exe's) by MaloverD07
https://gamejolt.com/games/td2dr_gamma/1054074 - v1101 - PC / Android (TD2DR Gamma Client) by w0nderEye
https://gamejolt.com/games/sonicexetiortd2d/857218 - v100 - PC (TD2DR Sonic over Exetior) by DavidDoesThings_44e6
https://gamejolt.com/games/project192116518312020112519/1034727 - v1101 - PC / Android (SCT: Project) by MatiMateo
https://gamejolt.com/games/td2drplus/941174 - v1101 - PC / Android (TD2DR+) by Banana8870
https://gamejolt.com/games/TD2DR-Origins-Expansion/970913 - v1101 - PC / Android (TD2DR X Metal Sonic) by FrostTheBurr
https://gamejolt.com/games/hellnbacktd2d/938656 - v1101 - PC / Android (TD2DR To Hell 'n Back) by kevin_the_bob-omb
https://gamejolt.com/games/theOtherSideOfUniverse/902979 - v100 - v1101 - PC (TD2DR: To The Other Side of Universe) by Hinerr
https://gamejolt.com/games/TD2DSonicEXETheSFactorProyectMOD/1004657 - v1101 - PC / Android (TD2DR: Sonic.EXE The S Factor Proyect) by SilverNight713
https://gamejolt.com/games/disasternm/977256 - v1101 - PC / Android (TD2DR Nightmare Multiverse) by SarkBobDemonPants
https://gamejolt.com/games/td2dr_maxs_maps/872256 - v100 - PC (TD2DR: Max's Map Pack (Metropolis v2) by ProMax
https://gamejolt.com/games/td2dohd/977499 - v1101 - PC / Android (TD2DR Other History) by Fo231xi
https://gamejolt.com/games/repentcastlemod/895008 - v100 - v1014 - Android (The Disaster 2D Remake Repent Castle Map - Android Port) by Miles3
https://gamejolt.com/games/VoidflatAndroid/899676 - v100 - Android (The Disaster 2D Remake Void Flat Custom Map - Android Port) by Miles3
https://gamejolt.com/games/Nooboversally_android/915614 - v100 - Android (TD2DR Noob over Sally) by Miles3
https://gamejolt.com/games/SonicExeTheDisaster2DRemakeAlternativeDimension/892055 - v100 - PC / Android (TD2DR Alternative Dimension) by GRNimoogi
https://gamejolt.com/games/v1014alternativedimension/916103 - v1014 - Android (TD2DR Alternative Dimension Beta Android Port) by Miles3
https://gamejolt.com/games/BETA-v1014-pc-alternative-dimension/911493 - v1014 - PC (TD2DR Alternative Dimension Port) by anormalperson_lol
"""

def parse_and_generate():
    mods = []

    for line in RAW_TEXT.strip().split('\n'):
        if not line.strip():
            continue

        author_match = re.search(r'by\s+(.+)$', line)
        if not author_match:
            continue
        author = author_match.group(1).strip()

        name_match = re.findall(r'\(([^)]+)\)', line[:author_match.start()])
        if name_match:
            mod_name = name_match[-1].strip()
            line_without_name = line[:author_match.start()].replace(f"({mod_name})", "")
        else:
            mod_name = "Unknown"
            line_without_name = line[:author_match.start()]

        urls = re.findall(r'https?://[^\s/]+/[^\s]+', line_without_name)
        urls = [u.strip('() -') for u in urls]

        versions = sorted(list(set(re.findall(r'v\d+', line_without_name))))

        tags = []
        if re.search(r'\bPC\b', line_without_name, re.IGNORECASE): tags.append("PC")
        if re.search(r'Android', line_without_name, re.IGNORECASE): tags.append("Android")

        status = "Active"
        if "development" in line.lower(): status = "WIP"
        elif "cancelled" in line.lower(): status = "Cancelled"

        links = []
        for url in urls:
            link_name = "Game Jolt" if "gamejolt" in url else "GitHub" if "github" in url else "GameBanana" if "gamebanana" in url else "Link"
            links.append(f"[{link_name}]({url})")
            
        mods.append({
            "name": mod_name,
            "author": author,
            "versions": versions,
            "tags": tags,
            "status": status,
            "links": " / ".join(links)
        })

    mods.sort(key=lambda x: (x["author"].lower(), x["name"].lower()))

    v1101, v1014, v100, others = [], [], [], []
    for m in mods:
        if "v1101" in m["versions"]: v1101.append(m)
        elif "v1014" in m["versions"]: v1014.append(m)
        elif "v100" in m["versions"]: v100.append(m)
        else: others.append(m)

    tables_md = ""
    
    def render_table(mod_list):
        if not mod_list: return ""
        table = "| Name | Author | Versions | Tags | Link | Status |\n"
        table += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
        for m in mod_list:
            v_str = ", ".join(m["versions"]) if m["versions"] else "—"
            t_str = ", ".join(m["tags"]) if m["tags"] else "—"
            table += f"| {m['name']} | {m['author']} | {v_str} | {t_str} | {m['links']} | {m['status']} |\n"
        return table + "\n"

    if v1101: tables_md += "### 🟢 Actual versions (v1.1.0.1)\n\n" + render_table(v1101) + "\n"
    if v1014: tables_md += "### 🟡 Beta versions (v1.0.1.4)\n\n" + render_table(v1014) + "\n"
    if v100: tables_md += "### 🔴 Old versions (v1.0.0)\n\n" + render_table(v100) + "\n"
    if others: tables_md += "### ⚪ Other / Without version\n\n" + render_table(others) + "\n"

    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except FileNotFoundError:
        readme_content = ""

    pattern = r'<!-- MODS_START -->.*?<!-- MODS_END -->'
    replacement = f"<!-- MODS_START -->\n{tables_md}<!-- MODS_END -->"
    
    if "<!-- MODS_START -->" in readme_content and "<!-- MODS_END -->" in readme_content:
        new_readme = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)
    else:
        new_readme = readme_content + "\n\n" + replacement

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
        print("README.md update!")

if __name__ == "__main__":
    parse_and_generate()

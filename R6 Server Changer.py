import os
import time
import getpass
import configparser
import CustomModule.VersionChecker

programVersion = "1.0.0"

os.system(f"title [XerosLab] R6 Server Changer - Version {programVersion}")

allServerListKR = ["Default", "미국 동부", "미국 중부", "미국 남중부", "미국 서부", "브라질 남부", "북유럽", "서유럽", "남아프리카 북부", "동아시아", "동남아시아", "호주 동부", "호주 남동부", "동일본"]
allServerListUS = ["default", "eastus", "centralus", "southcentralus", "westus", "brazilsouth", "northeurope", "westeurope", "southafricanorth", "eastasia", "southeastasia", "australiaeast", "australiasoutheast", "japaneast"]
configFileLocation = "C:\\Users\\{}\\Documents\\My Games\\Rainbow Six - Siege\\".format(getpass.getuser())
configFileLocation = os.path.join(configFileLocation, os.listdir(configFileLocation)[0], "GameSettings.ini")
config = configparser.ConfigParser()
config.read(configFileLocation)

def versionCheck():
    print(f"현재 프로그램 버전은 {programVersion}입니다.")
    lVersion = CustomModule.VersionChecker.versionChecker("r6serverchanger")
    if lVersion != programVersion:
        print(lVersion, programVersion)
        print("업데이트가 발견되었습니다.\n업데이트 다운로드 페이지로 이동합니다.")
        os.system("pause")
        os.system("start https://blog.xeros.dev/215")
    else:
        print("최신버전입니다.")
        time.sleep(2)

def printServerList():
    currentServer = config["ONLINE"]["DataCenterHint"]
    count = 1
    print(f"R6 Server Changer - Version {programVersion}")
    print("Copyrightⓒ2008 Xeros All rights reserved.       https://blog.xeros.dev\n")
    print("※ 반드시 게임을 종료한 상태에서 서버를 변경해주시기 바랍니다. ※")
    print("현재 적용되어있는 서버 : {}".format(currentServer))
    print("\n적용 가능한 서버 목록")
    for server in allServerListKR:
        print("{}. {}".format(count, server))
        count += 1

def main():
    versionCheck()
    while True:
        os.system("cls")
        printServerList()
        try:
            sel = int(input("> "))
        except ValueError:
            print("옳바른 숫자를 입력해주세요")
            print("잠시 뒤 서버 선택 화면으로 돌아갑니다.")
            time.sleep(3)
            continue
        if sel <= 0 or sel > len(allServerListKR):
            print("옳바른 숫자를 입력해주세요")
            print("잠시 뒤 서버 선택 화면으로 돌아갑니다.")
            time.sleep(3)
            continue
        else:
            selectedServer = allServerListUS[sel-1]
            config["ONLINE"]["DataCenterHint"] = selectedServer
            with open(configFileLocation, 'w', encoding="utf-8") as configfile:
                config.write(configfile)
            print("서버 설정이 완료되었습니다.")
            print("잠시 뒤 서버 선택 화면으로 돌아갑니다.")
            time.sleep(3)
            continue
main()
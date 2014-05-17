#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <string.h>
#include <time.h>
#include <sys/types.h>
#include <dirent.h>
#include <vector>
#include <algorithm>
#include "consoleHelper.h"

template <typename T,unsigned S>
inline unsigned arraysize(const T (&v)[S]) { return S; }

const std::string BASE_DIR = ".";
const Colors TITLE_CLR[] = {RED, GREEN, BLUE, YELLOW, PURPLE, CYAN};

std::vector<std::string> mods;

void mainMenu();
void repeat();
void compileMod(std::string modName);
void buildWorkspace(bool withSrc, std::string ide);

int main() {
    chdir(BASE_DIR.c_str());
    DIR* dirHandle;
    struct dirent * dirEntry;
    dirHandle = opendir(".\\modSrc");
    if( dirHandle ) {
        while( 0 != (dirEntry = readdir(dirHandle)) ) {
            if( strcmp(dirEntry->d_name, ".") == 0 || strcmp(dirEntry->d_name, "..") == 0 ) {
                continue;
            }
            mods.push_back(dirEntry->d_name);
        }

        closedir(dirHandle);
    }

    srand(time(0));
    mainMenu();
    return 0;
}

long cinLong() {
    std::string chStr = "";
    std::cin >> chStr;

    char* p;
    long converted = strtol(chStr.c_str(), &p, 0);

    return *p ? -1 : converted;
}

void repeat() {
    system("pause");
    system(CMD_CLEANSCREEN.c_str());
    mainMenu();
}

void mainMenu() {
    setColor(TITLE_CLR[rand() % arraysize(TITLE_CLR)]);
    std::cout << "---------------------------------------------------------------------------" << std::endl
              << "                     SanAndreasP's ForgeGradle Wrapper" << std::endl
              << "---------------------------------------------------------------------------" << std::endl;

    setColor(GRAY);
    std::cout << std::endl
              << " [1] build mod" << std::endl
              << " [2] setup workspace" << std::endl
              << " [3] use command line within gradle folder" << std::endl
              << " [4] show help" << std::endl
              << " [9] choose random text color [NYI]" << std::endl
              << " [0] exit" << std::endl
              << std::endl;

    setColor(WHITE);
    std::cout << "Please select a number: ";

    setColor(YELLOW);
    int chs = cinLong();
    setColor(WHITE);

    switch( chs ) {
        case 1:
            std::cout << std::endl << "Choose a mod from the list:" << std::endl;

            setColor(GRAY);
            for( unsigned int i = 0; i < mods.size(); i++ ) {
                std::cout << " [" << (i+1) << "] " << mods.at(i) << std::endl;
            }
            std::cout << " [" << mods.size() << "] Cancel" << std::endl;

            setColor(WHITE);
            std::cout << "> ";

            {
                setColor(YELLOW);
                long choice = cinLong()-1;
                setColor(WHITE);

                if( choice < 0 || choice >= (long)mods.size() ) {
                    std::cout << "No mod selected! Returning to main menu!" << std::endl;
                    repeat();
                    return;
                }

                compileMod(mods.at(choice));
                repeat();
                return;
            }
        case 2:
            std::cout << std::endl << "Build workspace" << std::endl;
            std::cout << "- With or without source? [Y/N] > ";
            {
                std::string input;
                std::cin >> input;
                std::transform(input.begin(), input.end(), input.begin(), ::tolower);

                bool withSrc = input.compare("y") == 0;

                std::cout << "- Which IDE? (e.g. 'eclipse') > ";
                std::string ide;
                std::cin >> ide;
                std::cout << std::endl;

                buildWorkspace(withSrc, ide);
                repeat();
                return;
            }

            return;
        case 3:
            system((CMD_CALL + " " + CMD_EXE).c_str());
            system(CMD_CLEANSCREEN.c_str());
            mainMenu();
            return;
        case 9:
            system(CMD_CLEANSCREEN.c_str());
            mainMenu();
            return;
        case 0:
            exit(0);
            return;
    }
    std::cout << "Invalid input! Try again!" << std::endl;
    repeat();
}

void compileMod(std::string modName) {
    chdir((".\\modSrc\\" + modName).c_str());
    system((CMD_CALL + " ..\\..\\gradlew build --stacktrace").c_str());
    chdir("..\\..\\");
}

void buildWorkspace(bool withSrc, std::string ide) {
    system((CMD_CALL + " gradlew clean").c_str());
    system((CMD_CALL + " gradlew cleanCache").c_str());
    if( withSrc ) {
        system((CMD_CALL + " gradlew setupDecompWorkspace --refresh-dependencies").c_str());
    } else {
        system((CMD_CALL + " gradlew setupDevWorkspace --refresh-dependencies").c_str());
    }
    system((CMD_CALL + " gradlew " + ide).c_str());
}

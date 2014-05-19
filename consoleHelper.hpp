#ifndef CONSOLEHELPER_HPP_INCLUDED
#define CONSOLEHELPER_HPP_INCLUDED
#include <windows.h>

enum Colors {
    RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, WHITE, GRAY
};

const std::string CMD_CALL = "CALL";
const std::string CMD_EXE = "cmd";
const std::string CMD_CLEANSCREEN = "CLS";

void setColorWnd(Colors color) {
    HANDLE hConsole = GetStdHandle (STD_OUTPUT_HANDLE);
    int fgColor = FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY;
    int bgColor = ~(BACKGROUND_RED | BACKGROUND_GREEN | BACKGROUND_BLUE);
    switch( color ) {
        case RED:
            fgColor = FOREGROUND_RED | FOREGROUND_INTENSITY;
            break;
        case GREEN:
            fgColor = FOREGROUND_GREEN | FOREGROUND_INTENSITY;
            break;
        case BLUE:
            fgColor = FOREGROUND_BLUE | FOREGROUND_INTENSITY;
            break;
        case YELLOW:
            fgColor = FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_INTENSITY;
            break;
        case PURPLE:
            fgColor = FOREGROUND_RED | FOREGROUND_BLUE | FOREGROUND_INTENSITY;
            break;
        case CYAN:
            fgColor = FOREGROUND_BLUE | FOREGROUND_GREEN | FOREGROUND_INTENSITY;
            break;
        case GRAY:
            fgColor = FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE;
            break;
        default:
            break;
    }
    SetConsoleTextAttribute(hConsole, fgColor & bgColor);
}

void setColor(Colors color) {
    // windows-only here!
    setColorWnd(color);
}

#endif // CONSOLEHELPER_HPP_INCLUDED

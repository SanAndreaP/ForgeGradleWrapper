#include "MainMenu.h"

#include <sstream>
#include <iomanip>
#include <string>
#include <wx/image.h>
#include <wx/bitmap.h>
#include <stdio.h>
#include "images/button_stpFrg.hpp"

//(*InternalHeaders(mainMenu)





//(*IdInit(mainMenu)






BEGIN_EVENT_TABLE(mainMenu,wxPanel)
	//(*EventTable(mainMenu)
	//*)
END_EVENT_TABLE()

mainMenu::mainMenu(wxWindow* parent,wxWindowID id,const wxPoint& pos,const wxSize& size)
{
	//(*Initialize(mainMenu)










	BitmapButton1->SetBitmap(wxBitmap(wxImage(buttonStpFrg::sizeX, buttonStpFrg::sizeY, buttonStpFrg::normal, true)));
	BitmapButton1->SetBitmapFocus(wxBitmap(wxImage(buttonStpFrg::sizeX, buttonStpFrg::sizeY, buttonStpFrg::normal, true)));
	BitmapButton1->SetBitmapDisabled(wxBitmap(wxImage(buttonStpFrg::sizeX, buttonStpFrg::sizeY, buttonStpFrg::normal, true)));
	BitmapButton1->SetBitmapHover(wxBitmap(wxImage(buttonStpFrg::sizeX, buttonStpFrg::sizeY, buttonStpFrg::hover, true)));
	BitmapButton2->SetBitmap(wxBitmap(wxImage(_T("C:\\Stuff\\C++ Projects\\ForgeGradleWrapper\\fGraleH_gui\\images\\button_stpFrg.png"))));
}

mainMenu::~mainMenu()
{
	//(*Destroy(mainMenu)
	//*)
}


void mainMenu::OnButton1Click(wxCommandEvent& event)
{
    wxImage img(_T("C:\\Stuff\\C++ Projects\\ForgeGradleWrapper\\fGraleH_gui\\images\\button_stpFrg.png"));
    unsigned long imgArea = img.GetWidth()*img.GetHeight();
    unsigned char *imgData = img.GetData();
    std::stringstream outp;
    for( unsigned long i = 0; i < imgArea*3L; i++ ) {
        outp << "\\x" << std::hex << (unsigned int)imgData[i];
    }
    this->TextCtrl1->SetValue(outp.str());
}
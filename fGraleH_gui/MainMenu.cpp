#include "MainMenu.h"

#include <sstream>
#include <iomanip>
#include <string>
#include <wx/image.h>
#include <wx/bitmap.h>
#include <stdio.h>
#include "images/button_stpFrg.hpp"

//(*InternalHeaders(mainMenu)
#include <wx/settings.h>
#include <wx/intl.h>
#include <wx/string.h>
//*)

//(*IdInit(mainMenu)
const long mainMenu::ID_BUTTON1 = wxNewId();
const long mainMenu::ID_TEXTCTRL1 = wxNewId();
const long mainMenu::ID_BITMAPBUTTON1 = wxNewId();
const long mainMenu::ID_PANEL1 = wxNewId();
//*)

BEGIN_EVENT_TABLE(mainMenu,wxPanel)
	//(*EventTable(mainMenu)
	//*)
END_EVENT_TABLE()

mainMenu::mainMenu(wxWindow* parent,wxWindowID id,const wxPoint& pos,const wxSize& size)
{
	//(*Initialize(mainMenu)
	Create(parent, wxID_ANY, wxDefaultPosition, wxSize(800,600), wxTAB_TRAVERSAL, _T("wxID_ANY"));
	Panel1 = new wxPanel(this, ID_PANEL1, wxPoint(0,0), wxSize(800,600), wxTAB_TRAVERSAL, _T("ID_PANEL1"));
	Button1 = new wxButton(Panel1, ID_BUTTON1, _("Label"), wxPoint(48,64), wxDefaultSize, 0, wxDefaultValidator, _T("ID_BUTTON1"));
	TextCtrl1 = new wxTextCtrl(Panel1, ID_TEXTCTRL1, _("Text"), wxPoint(160,16), wxSize(592,432), wxTE_MULTILINE, wxDefaultValidator, _T("ID_TEXTCTRL1"));
	BitmapButton1 = new wxBitmapButton(Panel1, ID_BITMAPBUTTON1, wxNullBitmap, wxPoint(136,496), wxSize(224,23), wxBU_AUTODRAW, wxDefaultValidator, _T("ID_BITMAPBUTTON1"));
	BitmapButton1->SetBackgroundColour(wxSystemSettings::GetColour(wxSYS_COLOUR_HIGHLIGHT));

	Connect(ID_BUTTON1,wxEVT_COMMAND_BUTTON_CLICKED,(wxObjectEventFunction)&mainMenu::OnButton1Click);
	//*)

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

#include "MainMenu.h"

#include <sstream>
#include <iomanip>
#include <string>
#include <wx/image.h>
#include <wx/bitmap.h>
#include <stdio.h>
#include "images/button_stpFrg.hpp"
#include "fGraleH_guiMain.h"

//(*InternalHeaders(mainMenu)
#include <wx/settings.h>
#include <wx/intl.h>
#include <wx/string.h>
//*)

//(*IdInit(mainMenu)
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
	Create(parent, id, wxDefaultPosition, wxSize(800,600), wxTAB_TRAVERSAL, _T("id"));
	Panel1 = new wxPanel(this, ID_PANEL1, wxPoint(0,0), wxSize(800,600), wxTAB_TRAVERSAL, _T("ID_PANEL1"));
	BitmapButton1 = new wxBitmapButton(Panel1, ID_BITMAPBUTTON1, wxNullBitmap, wxPoint(272,24), wxSize(224,23), wxBU_AUTODRAW, wxDefaultValidator, _T("ID_BITMAPBUTTON1"));
	BitmapButton1->SetBackgroundColour(wxSystemSettings::GetColour(wxSYS_COLOUR_HIGHLIGHT));

	Connect(ID_BITMAPBUTTON1,wxEVT_COMMAND_BUTTON_CLICKED,(wxObjectEventFunction)&mainMenu::OnBitmapButton1Click);
	//*)

	BitmapButton1->SetBitmap(wxBitmap(buttonSetupFrg::getNormal()));
	BitmapButton1->SetBitmapFocus(wxBitmap(buttonSetupFrg::getFocused()));
	BitmapButton1->SetBitmapDisabled(wxBitmap(buttonSetupFrg::getDisabled()));
	BitmapButton1->SetBitmapHover(wxBitmap(buttonSetupFrg::getHovered()));
}

mainMenu::~mainMenu()
{
	//(*Destroy(mainMenu)
	//*)
}

void mainMenu::OnBitmapButton1Click(wxCommandEvent& event)
{
    this->Hide();
    ((fGraleH_guiFrame*)this->GetParent())->changePanel(fGraleH_guiFrame::Panels::STP_FORGE);
}

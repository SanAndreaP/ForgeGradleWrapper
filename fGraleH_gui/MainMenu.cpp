#include "MainMenu.h"

//(*InternalHeaders(MainMenu)
#include <wx/settings.h>
#include <wx/intl.h>
#include <wx/string.h>
//*)

//(*IdInit(MainMenu)
//*)

BEGIN_EVENT_TABLE(MainMenu,wxPanel)
	//(*EventTable(MainMenu)
	//*)
END_EVENT_TABLE()

MainMenu::MainMenu(wxWindow* parent,wxWindowID id,const wxPoint& pos,const wxSize& size)
{
	//(*Initialize(MainMenu)
	Create(parent, id, wxDefaultPosition, wxSize(411,373), wxTAB_TRAVERSAL, _T("id"));
	SetBackgroundColour(wxSystemSettings::GetColour(wxSYS_COLOUR_HIGHLIGHT));
	//*)
}

MainMenu::~MainMenu()
{
	//(*Destroy(MainMenu)
	//*)
}


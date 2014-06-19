#ifndef MAINMENU_H
#define MAINMENU_H

//(*Headers(MainMenu)
#include <wx/panel.h>
//*)

class MainMenu: public wxPanel
{
	public:

		MainMenu(wxWindow* parent,wxWindowID id=wxID_ANY,const wxPoint& pos=wxDefaultPosition,const wxSize& size=wxDefaultSize);
		virtual ~MainMenu();

		//(*Declarations(MainMenu)
		//*)

	protected:

		//(*Identifiers(MainMenu)
		//*)

	private:

		//(*Handlers(MainMenu)
		//*)

		DECLARE_EVENT_TABLE()
};

#endif

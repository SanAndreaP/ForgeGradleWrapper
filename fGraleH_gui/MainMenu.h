#ifndef MAINMENU_H
#define MAINMENU_H

//(*Headers(mainMenu)
#include <wx/panel.h>
#include <wx/bmpbuttn.h>
//*)

class mainMenu: public wxPanel
{
	public:

		mainMenu(wxWindow* parent,wxWindowID id=wxID_ANY,const wxPoint& pos=wxDefaultPosition,const wxSize& size=wxDefaultSize);
		virtual ~mainMenu();

		//(*Declarations(mainMenu)
		wxPanel* Panel1;
		wxBitmapButton* BitmapButton1;
		//*)

	protected:

		//(*Identifiers(mainMenu)
		static const long ID_BITMAPBUTTON1;
		static const long ID_PANEL1;
		//*)

	private:

		//(*Handlers(mainMenu)
		void OnBitmapButton1Click(wxCommandEvent& event);
		//*)

		DECLARE_EVENT_TABLE()
};

#endif

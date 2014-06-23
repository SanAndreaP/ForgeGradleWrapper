#ifndef MAINMENU_H
#define MAINMENU_H

//(*Headers(mainMenu)
#include <wx/textctrl.h>
#include <wx/panel.h>
#include <wx/bmpbuttn.h>
#include <wx/button.h>
//*)

class mainMenu: public wxPanel
{
	public:

		mainMenu(wxWindow* parent,wxWindowID id=wxID_ANY,const wxPoint& pos=wxDefaultPosition,const wxSize& size=wxDefaultSize);
		virtual ~mainMenu();

		//(*Declarations(mainMenu)
		wxButton* Button1;
		wxPanel* Panel1;
		wxBitmapButton* BitmapButton1;
		wxTextCtrl* TextCtrl1;
		//*)

	protected:

		//(*Identifiers(mainMenu)
		static const long ID_BUTTON1;
		static const long ID_TEXTCTRL1;
		static const long ID_BITMAPBUTTON1;
		static const long ID_PANEL1;
		//*)

	private:

		//(*Handlers(mainMenu)
		void OnButton1Click(wxCommandEvent& event);
		//*)

		DECLARE_EVENT_TABLE()
};

#endif

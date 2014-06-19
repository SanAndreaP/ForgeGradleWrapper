#ifndef SETUPFORGE_H
#define SETUPFORGE_H

//(*Headers(setupForge)
#include <wx/textctrl.h>
#include <wx/panel.h>
#include <wx/richtext/richtextctrl.h>
//*)

class setupForge: public wxPanel
{
	public:

		setupForge(wxWindow* parent,wxWindowID id=wxID_ANY,const wxPoint& pos=wxDefaultPosition,const wxSize& size=wxDefaultSize);
		virtual ~setupForge();

		//(*Declarations(setupForge)
		wxRichTextCtrl* RichTextCtrl1;
		wxTextCtrl* TextCtrl1;
		//*)

	protected:

		//(*Identifiers(setupForge)
		static const long ID_TEXTCTRL1;
		static const long ID_RICHTEXTCTRL1;
		//*)

	private:

		//(*Handlers(setupForge)
		//*)

		DECLARE_EVENT_TABLE()
};

#endif

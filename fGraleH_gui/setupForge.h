#ifndef SETUPFORGE_H
#define SETUPFORGE_H

//(*Headers(setupForge)
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
		wxPanel* Panel1;
		//*)

	protected:

		//(*Identifiers(setupForge)
		static const long ID_RICHTEXTCTRL1;
		static const long ID_PANEL1;
		//*)

	private:

		//(*Handlers(setupForge)
		void OnBitmapButton1Click(wxCommandEvent& event);
		//*)

		DECLARE_EVENT_TABLE()
};

#endif

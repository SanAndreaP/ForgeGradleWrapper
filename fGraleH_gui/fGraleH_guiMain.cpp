/***************************************************************
 * Name:      fGraleH_guiMain.cpp
 * Purpose:   Code for Application Frame
 * Author:    SanAndreasP ()
 * Created:   2014-06-18
 * Copyright: SanAndreasP ()
 * License:
 **************************************************************/

#include "fGraleH_guiMain.h"
#include <wx/msgdlg.h>

//(*InternalHeaders(fGraleH_guiFrame)
#include <wx/intl.h>
#include <wx/string.h>
//*)

//helper functions
enum wxbuildinfoformat {
    short_f, long_f };

wxString wxbuildinfo(wxbuildinfoformat format)
{
    wxString wxbuild(wxVERSION_STRING);

    if (format == long_f )
    {
#if defined(__WXMSW__)
        wxbuild << _T("-Windows");
#elif defined(__UNIX__)
        wxbuild << _T("-Linux");
#endif

#if wxUSE_UNICODE
        wxbuild << _T("-Unicode build");
#else
        wxbuild << _T("-ANSI build");
#endif // wxUSE_UNICODE
    }

    return wxbuild;
}

//(*IdInit(fGraleH_guiFrame)
const long fGraleH_guiFrame::ID_PANEL1 = wxNewId();
//*)

BEGIN_EVENT_TABLE(fGraleH_guiFrame,wxFrame)
    //(*EventTable(fGraleH_guiFrame)
    //*)
END_EVENT_TABLE()

fGraleH_guiFrame::fGraleH_guiFrame(wxWindow* parent,wxWindowID id)
{
    //(*Initialize(fGraleH_guiFrame)
    Create(parent, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxDEFAULT_DIALOG_STYLE|wxCLOSE_BOX|wxFRAME_SHAPED|wxMINIMIZE_BOX, _T("wxID_ANY"));
    SetClientSize(wxSize(800,600));
    P_Main = new wxPanel(this, ID_PANEL1, wxDefaultPosition, wxSize(800,600), wxTAB_TRAVERSAL, _T("ID_PANEL1"));
    //*)

    this->SetClientSize(this->P_Main->GetSize());
    this->CenterOnScreen();
    this->m_panels.insert(std::pair<Panels, wxPanel*>(Panels::MAIN_MENU, new mainMenu(this->P_Main)));
    this->m_panels.insert(std::pair<Panels, wxPanel*>(Panels::STP_FORGE, new setupForge(this->P_Main)));

    this->changePanel(Panels::MAIN_MENU);

//    this->m_panels.at(Panels::STP_FORGE)->Hide();
}

fGraleH_guiFrame::~fGraleH_guiFrame()
{
    //(*Destroy(fGraleH_guiFrame)
    //*)
}

void fGraleH_guiFrame::OnQuit(wxCommandEvent& event)
{
    Close();
}

void fGraleH_guiFrame::OnAbout(wxCommandEvent& event)
{
    wxString msg = wxbuildinfo(long_f);
    wxMessageBox(msg, _("Welcome to..."));
}


void fGraleH_guiFrame::OnResize(wxSizeEvent& event)
{
    event.Skip();
}

void fGraleH_guiFrame::changePanel(Panels panel)
{
    for( std::pair<Panels, wxPanel*> elem : this->m_panels ) {
        if( elem.first == panel ) {
            elem.second->Show();
        } else {
            elem.second->Hide();
        }
    }
}

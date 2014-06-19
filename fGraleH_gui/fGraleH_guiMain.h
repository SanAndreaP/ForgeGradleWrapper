/***************************************************************
 * Name:      fGraleH_guiMain.h
 * Purpose:   Defines Application Frame
 * Author:    SanAndreasP ()
 * Created:   2014-06-18
 * Copyright: SanAndreasP ()
 * License:
 **************************************************************/

#ifndef FGRALEH_GUIMAIN_H
#define FGRALEH_GUIMAIN_H

//(*Headers(fGraleH_guiFrame)
#include <wx/panel.h>
#include <wx/frame.h>
//*)
#include "setupForge.h"

class fGraleH_guiFrame: public wxFrame
{
    public:

        fGraleH_guiFrame(wxWindow* parent,wxWindowID id = -1);
        virtual ~fGraleH_guiFrame();

    private:

        //(*Handlers(fGraleH_guiFrame)
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        void OnResize(wxSizeEvent& event);
        //*)

        //(*Identifiers(fGraleH_guiFrame)
        static const long ID_PANEL1;
        //*)

        //(*Declarations(fGraleH_guiFrame)
        wxPanel* Panel1;
        //*)

        wxPanel* P_SetupForge;

        DECLARE_EVENT_TABLE()
};

#endif // FGRALEH_GUIMAIN_H

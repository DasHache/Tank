#include <frame.h>

Frame::Frame(const wxString& title)
	: wxFrame(NULL, wxID_ANY, title, wxDefaultPosition, wxSize(250, 150))
{
	Centre();
}

Frame* Frame::make_frame() 
{
	Frame* f = new Frame("Tank");
	return f;
}



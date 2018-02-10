#include <wx/wx.h>

class Frame : public wxFrame
{
private:
	Frame(const wxString& title);

public:
	static Frame* make_frame();
};




import cv2
import gi

gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf

cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 400)

class TakePicture:
    def on_windowCamera_destroy(self, *args):
        Gtk.main_quit()
        
    def on_btnSaveImage_clicked(self, *args):
        textName = builder.get_object("entryImgName")
        entryName = (textName.get_text())
        
        if (textName.get_text() == ""):
            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonType.OK, "Name Cannot Be Empty")
            dialog.run()
            dialog.destroy()
        else:
            ret, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite("imageCapture/" + entryName + ".jpg", frame)
            image2.set_from_file("imageCapture/" + entryName + ".jpg")
            
def show_frame(*args):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    framecp = frame.copy()
    
    pb = GdkPixbuf.Pixbuf.new_from_data(framecp.tobytes(),
                                        GdkPixbuf.Colorspace.RGB,
                                        False,
                                        8,
                                        framecp.shape[1],
                                        framecp.shape[0],
                                        framecp.shape[2]*framecp.shape[1])
    
    image1.set_from_pixbuf(pb.copy())
    return True
    
builder = Gtk.Builder()
builder.add_from_file("handlingCamera.glade")
window = builder.get_object("windowCamera")
image1 = builder.get_object("imgOri")
image2 = builder.get_object("imgVerify")
window.show_all()

builder.connect_signals(TakePicture())
GLib.idle_add(show_frame)
Gtk.main()
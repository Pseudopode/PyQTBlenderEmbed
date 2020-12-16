# PyQTBlenderEmbed

![Title Screen] (./docs/imgs/0_simple_embedding.jpg "")

Examples to show how to embed the Blender windows in a PyQT app, on **windows**.

You must have a Blender version installed on your drive, and a working PyQT installation

# Example 0 - '0_simple_embedding'

Simple example showing how to start Blender as a subprocess, grab is handle, and reparent its window as a QWindow.

In the QApplication you have a QHBoxLayout, with the Blender view on the left, and a QWebEngineView on the right hand side.

This QWebEngineView load a *page.html* file, placed in the same folder as the Python script.

Don't forget to change the folder path of your Blender if you installed it somewhere else than the standard installation folder.

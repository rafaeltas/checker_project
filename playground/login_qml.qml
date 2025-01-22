import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material


ApplicationWindow {
  visible: true
  width: 500
  height: 500
  Material.theme: 'Dark'
  font.pixelSize: 24

  Button {
    text: 'Botão'
    anchors.verticalCenter: parent.verticalCenter
    anchors.horizontalCenter: parent.horizontalCenter
    width: 200
    height: 100
  }
}

#---------------------------------------------------------------------------
# 参照

from xoxxox.libmid import LibMid

#---------------------------------------------------------------------------
# 処理：操作：文字列

class OpeStr:

  # 機能：文字列の、最初の文字を返す
  @staticmethod
  def strcar(datorg):
    strorg = datorg.decode("utf-8")
    strnew = strorg[0]
    datnew = strnew.encode("utf-8")
    return datnew

  # 機能：文字列の、最初の文字を除いた残りの文字列を返す
  @staticmethod
  def strcdr(datorg):
    strorg = datorg.decode("utf-8")
    strnew = strorg[1:]
    datnew = strnew.encode("utf-8")
    return datnew

  # 機能：文字列群を連結し、返す
  @staticmethod
  def strcat(datcar, datcdr):
    strcar = datcar.decode("utf-8")
    strcdr = datcdr.decode("utf-8")
    strcat = strcar + strcdr
    datcat = strcat.encode("utf-8")
    return datcat

LibMid.dicprc["xoxxox.OpeStr.strcar"] = {"frm": "xoxxox_libstr.OpeStr.strcar", "arg": ["keymmd"], "syn": True}
LibMid.dicprc["xoxxox.OpeStr.strcdr"] = {"frm": "xoxxox_libstr.OpeStr.strcdr", "arg": ["keymmd"], "syn": True}
LibMid.dicprc["xoxxox.OpeStr.strcat"] = {"frm": "xoxxox_libstr.OpeStr.strcat", "arg": ["keymmd", "keycdr"], "syn": True}

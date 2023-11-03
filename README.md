# bch_imae
Descarga automatizada del IMAE de Honduras por subcategoría o serie global a traves del portal: Sistema del IMAE (SISEE). https://sisee.bch.hn/IMAE/

```python
# Usage example
session = descargar_IMAE('C:\\USERS\\PATH\\DIR')
session.login('gabriela123', 'gabriela123')
session.descargar_IMAE_query(global_only=False)
data = session.view_download(delete_file=False)
display(data)
```

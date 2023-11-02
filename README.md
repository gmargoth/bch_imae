# bch_imae
Descarga automatizada del IMAE de Honduras por subcategoría o serie global a traves del portal: Sistema del IMAE (SISEE). https://sisee.bch.hn/IMAE/

```python
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
save_to = 'C:\\YOUR\\USER\\PATH\\DIR\\'
session = login_SISEE(username, password, save_to)

global_only = False
downaload_IMAE_query(session, global_only)
session.quit()
```

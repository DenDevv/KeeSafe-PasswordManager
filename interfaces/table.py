from utils.keesafe_module import KeeSafe


class TableData():
    def data_table(self):
        ks = KeeSafe()
        items = ks.show_all_data()
        db = []

        for item in items:
            r_id = item[0]
            name = item[1]
            login = item[2]
            passw = "{hiden}"
            url = item[4]

            db.append((r_id, name, login, passw, url,))
        return db
from Connector import sql_connect
import datetime
connection_to_config = sql_connect('db_config_data_w')
config = connection_to_config.cursor()
connection_to_dimen = sql_connect('db_dimensional')
dimen = connection_to_dimen.cursor()
connection_to_source = sql_connect('db_supermarket')
source = connection_to_source.cursor()


qCountTableDimensional = "SELECT count(*) from information_schema.TABLES where TABLE_SCHEMA = 'db_dimensional'"
qCountTableConfig = "SELECT COUNT(*) FROM tb_info_table"

qGetTableDimensional = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'db_dimensional' "

qInsertTableConfig = "INSERT INTO tb_info_table(nama_table) VALUES('%s')"


#==============BATCH INFO UPDATE TABLE===============#
qGetBatchInfo = "SELECT COUNT(*) FROM update_log"
qGEtTimeNow = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')


#================== Analyze Table====================#



class UpdateConfig:

    def __init__(self):
        self.get_table_from_dimen()

        pass



    def get_last_update(self):

        pass

    def analyze_table(self):

        pass


    def get_table_from_dimen(self):

        dimen.execute(qCountTableDimensional)
        config.execute(qCountTableConfig)
        count_table_dimen = dimen.fetchone()
        count_table_config = config.fetchone()
        count_table_dimen = int(count_table_dimen[0])
        count_table_config = int(count_table_config[0 ])


        if count_table_dimen > count_table_config:
            dimen.execute(qGetTableDimensional)

            val = dimen

            for x in val.fetchall():
                val_table = "".join(x)
                print(val_table)
                config.execute(qInsertTableConfig%val_table)
                connection_to_config.commit()
        else:
            print("table sudah up todated")



        pass


def main():
    UpdateConfig()


if __name__ == "__main__":
    main()
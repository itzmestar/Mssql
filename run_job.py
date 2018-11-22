import argparse
import platform, logging, os
import _mssql

#########Logging configuration##########
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(__file__))[0]+'.log')
else:
    logging_file = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(__file__))[0]+'.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(threadName)-9s : %(message)s',
    filename=logging_file,
    filemode='w',
)
#########Logging configuration ends##########

__version__ = "2.0"

SERVER='192.168.1.12'
USER='runjobs'
PASS='password'
DATABASE='testDB'
STORED_PROC='AAA_Test'

class Mssql():
    def __init__(self, server, user, password, database):
        self.server = server
        self.password = password
        self.user = user
        self.database = database

    def run(self, stored_procedure):
        '''
        Run the stored procedure.
        '''
        try:
            # connect to mssql server
            with _mssql.connect(server=self.server, user=self.user,
                                password=self.password, database=self.database) as conn:
                logging.debug("DB connection successful")
                try:
                    # execute the stored procedure
                    conn.execute_query(stored_procedure)
                    logging.debug("Stored Procedure: {} execution successful!".format(stored_procedure))
                except Exception as error:
                    logging.error("Stored Procedure: {} execution failed!".format(stored_procedure))
        except Exception as error:
            logging.error("DB connection failed: ")


def main():
    mssql = Mssql(SERVER, USER, PASS, DATABASE)
    mssql.run(STORED_PROC)

if __name__ == "__main__":
    """
    Execution starts here.
    """

    '''
    parser = argparse.ArgumentParser(description='Run SQL script.')
    parser.add_argument('-s', '--sql', help='SQL filename', type=str, required=True)
    parser.add_argument('-u', '--user', help='Oracle user', type=str)
    args = parser.parse_args()

    column=args.col
    search_string=args.str
    '''
    main()

    

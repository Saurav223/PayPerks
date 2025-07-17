import hashlib
from db_connector import create_connection

class DatabaseManager:
    def __init__(self):
        try:
            self.conn = create_connection()
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Failed to initialize database connection:", e)
            self.conn = None
            self.cursor = None

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            print("Error closing connection:", e)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users_table (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            dob DATE DEFAULT NULL,
            address VARCHAR(255) DEFAULT NULL,
            phone_number VARCHAR(15) DEFAULT NULL,
            type_of_id ENUM('passport', 'driver_license', 'citizenship') DEFAULT NULL,
            id_number VARCHAR(50) DEFAULT NULL,
            balance DECIMAL(10, 2) DEFAULT 0.00,
            reward_points INT DEFAULT 0,
            income DECIMAL(10, 2) DEFAULT 0.00,
            expenses DECIMAL(10, 2) DEFAULT 0.00,
            is_verified BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print("Error creating users_table:", e)

    def create_transactions_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS transactions_table (
            transaction_id INT AUTO_INCREMENT PRIMARY KEY,
            sender_id INT NOT NULL,
            receiver_id INT NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            description VARCHAR(255) DEFAULT NULL,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (sender_id) REFERENCES users_table(user_id),
            FOREIGN KEY (receiver_id) REFERENCES users_table(user_id)
        );
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print("Error creating transactions_table:", e)

    def create_rewards_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS rewards_table (
            reward_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            points INT NOT NULL,
            source_transaction_id INT DEFAULT NULL,
            reward_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users_table(user_id),
            FOREIGN KEY (source_transaction_id) REFERENCES transactions_table(transaction_id)
        );
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print("Error creating rewards_table:", e)

    def create_deposits_or_payments_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS deposits_or_payments (
            deposite_pay_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            transaction_type ENUM('deposit', 'payment') NOT NULL,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            description VARCHAR(255) DEFAULT NULL,
            FOREIGN KEY (user_id) REFERENCES users_table(user_id)
        );
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print("Error creating deposits_or_payments table:", e)

    def hash_password(self, password):
        try:
            return hashlib.sha256(password.encode()).hexdigest()
        except Exception as e:
            print("Password hashing failed:", e)
            return None

    def register_user(self, full_name,email,password):
        try:
            hashed_pw = self.hash_password(password)
            if not hashed_pw:
                raise ValueError("Hashing failed")
            query = 'INSERT INTO users_table (full_name, password_hash, email) VALUES (%s, %s, %s)'
            self.cursor.execute(query, (full_name, hashed_pw, email))
            self.conn.commit()
            return True
        except Exception as e:
            print("User registration failed:", e)
            return False

    def authenticate_user(self, email, password):
        try:
            query = 'SELECT password_hash FROM users_table WHERE email = %s'
            self.cursor.execute(query, (email,))
            result = self.cursor.fetchone()
            if result:
                stored_hash = result[0]
                input_hash = self.hash_password(password)
                return input_hash == stored_hash
            return False
        except Exception as e:
            print("Authentication error:", e)
            return False

    def get_user_by_email(self, email):
        try:
            query = 'SELECT full_name, balance, reward_points, income, expenses, user_id FROM users_table WHERE email = %s'
            self.cursor.execute(query, (email,))
            return self.cursor.fetchone()
        except Exception as e:
            print("Error fetching user by email:", e)
            return None
        
    def email_exists(self, email):
        try:
            query = 'SELECT 1 FROM users_table WHERE email = %s'
            self.cursor.execute(query, (email,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print("Email check failed:", e)
            return False

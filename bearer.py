�
    �1sc�  �                   �P   � d dl Z d dlZdddddddd	d
dddddd�ZdZddiZd� Zd� ZdS )�    Nzsecuretoken.googleapis.comz*/*zid-ID,id;q=0.9zhttps://taki.appzhttps://taki.app/z@"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"z?0z	"Windows"�empty�corsz
cross-sitezoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36z$Chrome/JsCore/9.9.2/FirebaseCore-webz)1:616358120246:web:6cde3d1fd3f9030f244197)�	authority�acceptzaccept-language�origin�refererz	sec-ch-uazsec-ch-ua-mobilezsec-ch-ua-platformzsec-fetch-destzsec-fetch-modezsec-fetch-sitez
user-agentzx-client-versionzx-firebase-gmpidz"https://securetoken.googleapis.com�key�'AIzaSyBU3QRNyo_ugyLIlCj_aN9sykVsSlOJZ2Qc                 �.   � t          j        | �  �        }|S )N)�json�loads)�data�values     �	bearer.py�	load_jsonr      s   � ��J�t���E��L�    c                 �   � d| d�}t          j        t          dz   t          |t          ��  �        }t          |j        �                    �   �         �  �        d         S )N�refresh_token)�
grant_typer   z	/v1/token)�headersr   �params�id_token)�requests�post�hostr   r   r   �content�decode)�tokenr   �reqs      r   �ambil_bearerr       sT   � �%��� �D� �-��[�(�'��V�
T�
T�
T�C��S�[�'�'�)�)�*�*�:�6�6r   )r   r   r   r   r   r   r    � r   r   �<module>r"      s�   �� ���� ���� .��'� �"�S��%���"� D�>�C�� ��  ,���<�

��� � �7� 7� 7� 7� 7r   


# Setting no proxy for "host"
os.environ['NO_PROXY'] = host

--------------------------------------------------------------------------------------------------------------------

requests library
________________


# General Format
response = requests.request(method, url, **kwargs)

#The optional arguments:
  * params -- (GET) Dictionary or bytes to be sent in the query string for the Request.
  * data -- (POST) Dictionary or list of tuples [(key, value)] (will be form-encoded), bytes, 
              or file-like object to send in the body of the Request.
  * Headers --  Dictionary of HTTP Headers to send with the Request.
  * verify --  Either a boolean, in which case it controls whether we verify the server's 
              TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to True.
  * allow_redirects (bool) -- Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.
  
# response contains:
  * content - Content of the response, in bytes.
  * status_code - status code of the response (e.g., 200, 404,301)
  * headers  -  headers of the response
  
  
  
  
  
# convert to Ascii to unicode
s = uri
uri_hex = "00".join("{:02x}".format(ord(c)) for c in s)

#Ctypes data


C Type Python Type ctypes Type
char 1-character string c_char
wchar_t 1-character Unicode string c_wchar
char int/long c_byte
char int/long c_ubyte
short int/long c_short
unsigned short int/long c_ushort
int int/long C_int
unsigned int int/long c_uint
long int/long c_long
unsigned long int/long c_ulong
long long int/long c_longlong
unsigned long long int/long c_ulonglong
float float c_float
double float c_double
char * (NULL terminated) string or none c_char_p
wchar_t * (NULL terminated) unicode or none c_wchar_p
void * int/long or none c_void_p

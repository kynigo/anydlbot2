class Translation(object):
    START_TEXT = """<b>ഹേയ്! ഞാൻ @world_wide_movies എന്ന ചാനലിന്റെ യന്ത്രമനുഷ്യൻ .എന്നെ എങ്ങനെ ഉപയോഗിക്കണമെന്ന് അറിയാൻ /help ക്ലിക്ക് ചെയ്യുക.
    </b>.\n
     
    <i> കുറച്ചൊക്കെ ഞാൻ മലയാളത്തിൽ പറഞ്ഞു തരാം :)</i>"""
    RENAME_403_ERR = "<b>ക്ഷമിക്കണം. ഈ ഫയലിന്റെ പേരുമാറ്റാൻ നിങ്ങൾക്ക് അനുവാദമില്ല.</b>"
    ABS_TEXT = " <b>ദയവായി സ്വാർത്ഥനാകരുത്.</b>"
    UPGRADE_TEXT = "<b>നിങ്ങൾ എന്റെ സുഹൃത്താണെങ്കിൽ ഈ ബോട്ട് ഉപയോഗിക്കാൻ സൌജന്യമാണ്......</b>"
    FORMAT_SELECTION = "<b>ആവശ്യമുള്ള ഫോർമാറ്റ് തിരഞ്ഞെടുക്കുക:</b> "
    SET_CUSTOM_USERNAME_PASSWORD = """<b>നിങ്ങൾക്ക് പ്രീമിയം വീഡിയോകൾ ഡൗൺലോഡ് ചെയ്യണമെങ്കിൽ, ഇനിപ്പറയുന്ന ഫോർമാറ്റിൽ നൽകുക:
URL | filename | username | password</b>"""
    NOYES_URL = "<b>ഇതൊരു സാവധാനത്തിലുള്ള ലിങ്കാണ് ബ്രോ! ഞാൻ ഇതിനുവേണ്ടി എന്റെ സമയം പാഴാക്കുകയില്ല. എനിക്ക് ഒരു ഫാസ്റ്റ് ലിങ്ക് തരൂ<</b>"
    DOWNLOAD_START = "<b>നിങ്ങളുടെ ഫയലുകൾ ഡൗൺലോഡ് ചെയ്യുന്നു.....📥\n\nഇത്തിരി നേരം വെയിറ്റ് ചെയ്യൂ</b>"
    UPLOAD_START = "<b>നിങ്ങളുടെ ഫയലുകൾ അപ്‌ലോഡ് ചെയ്യുന്നു.....📤📤\n\nഇപ്പ ശെരിയാക്കി തര </b>"
    RCHD_BOT_API_LIMIT ="<b>അനുവദനീയമായ പരമാവധി വലുപ്പത്തേക്കാൾ വലുത്. എന്നിരുന്നാലും, അപ്‌ലോഡ് ചെയ്യാൻ ശ്രമിക്കുന്നു.</b>"
    RCHD_TG_API_LIMIT = "ഡൗൺലോഡ് ചെയ്തു {} സെക്കന്റ് കൊണ്ട്.\nDetected File Size: {}\n<b>ക്ഷമിക്കണം. പക്ഷേ, ടെലിഗ്രാം API പരിമിതികൾ കാരണം എനിക്ക് 2GB-യിൽ കൂടുതൽ ഫയലുകൾ അപ്‌ലോഡ് ചെയ്യാൻ കഴിയില്ല.</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>ഫയൽ അപ്‌ലോഡ് ചെയ്‌തു</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "ഇത് ചെയ്യാൻ നിങ്ങൾക്ക് അധികാരമില്ല. ഇത് <b>അഡ്മിൻ</b> വേണ്ടി മാത്രം"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "ഫയൽ വലുപ്പം കണ്ടെത്തി: {}. സൗജന്യ ഉപയോക്താക്കൾക്ക് ഈ ഫയൽ വലുപ്പം മാത്രമേ അപ്‌ലോഡ് ചെയ്യാനാകൂ: {}\nനിങ്ങളുടെ സബ്‌സ്‌ക്രിപ്‌ഷൻ /upgrade ചെയ്യുക."
    SAVED_CUSTOM_THUMB_NAIL = "<b>ഇഷ്‌ടാനുസൃത വീഡിയോ / ഫയൽ ലഘുചിത്രം എടുത്ത് വെച്ചു . ഈ ചിത്രം വീഡിയോ / ഫയലിൽ ഉപയോഗിക്കും.</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ <b>ഇഷ്‌ടാനുസൃത ലഘുചിത്രം വിജയകരമായി മായ്‌ച്ചു."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ മീഡിയ വിജയകരമായി മായ്ച്ചു.</b>"
    SAVED_RECVD_DOC_FILE = "<b>പ്രമാണം ഡൗൺലോഡ് ചെയ്തു.</b>"
    CUSTOM_CAPTION_UL_FILE = " <b>ബോട്ട് സൃഷ്ടിച്ചത് \n   👉**@DevAXD**</b>"
    NO_CUSTOM_THUMB_NAIL_FOUND = "<b>ഇഷ്‌ടാനുസൃത ലഘുചിത്രമൊന്നും കണ്ടെത്തിയില്ല .</b>"
    NO_VOID_FORMAT_FOUND = "നിങ്ങൾക്ക് ലിങ്ക്  പരിശോധിക്കാമോ? <b>URL-ൽ നിന്ന് വീഡിയോ ഫോർമാറ്റ് കണ്ടെത്താൻ എനിക്ക് കഴിയുന്നില്ല."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """നിലവിലെ പ്ലാൻ വിശദാംശങ്ങൾ
-----------------------------
➪ടെലിഗ്രാം ഐഡി: <code>{}</code>
➪പ്ലാൻ പേര്: 75GB Per Month
➪കാലഹരണപ്പെടുന്നത്: 1/12/2023
-----------------------------"""
    HELP_USER = """<b>എനിക്ക് ചെയ്യാൻ കഴിയുന്ന ഒന്നിലധികം കാര്യങ്ങൾ ഉണ്ട്:</b>\n\n
    
    <b>[YTDLp] പിന്തുണയ്ക്കുന്ന എല്ലാ വീഡിയോ ഫോർമാറ്റുകളും</b>
➪  <b>ഏതെങ്കിലും നേരിട്ടുള്ള ലിങ്കിൽ നിന്ന് ഫയലായി അപ്‌ലോഡ് ചെയ്യുക</b>
➪  <b>ഇഷ്‌ടാനുസൃത ലഘുചിത്ര പിന്തുണയോടെ ടെലിഗ്രാം ഫയലുകൾ പുനർനാമകരണം ചെയ്യുക.\n /rename ഫയലിനു മറുപടിയായി നൽകുക </b>
➪  <b>ഏതൊരു ടെലിഗ്രാം ഫയലിന്റെയും ഹൈ സ്പീഡ് ഡയറക്ട് ഡൗൺലോഡ് ലിങ്ക് നേടുക.\nReply /getlink ഫയലിനു മറുപടിയായി നൽകുക</b>
-----------------------------

നിങ്ങളുടെ നിലവിലെ പ്ലാൻ വിശദാംശങ്ങൾ അറിയാൻ /m അയയ്ക്കുക"""
    REPLY_TO_DOC_GET_LINK = "<b>ഏതൊരു ടെലിഗ്രാം ഫയലിന്റെയും ഹൈ സ്പീഡ് ഡയറക്ട് ഡൗൺലോഡ് ലിങ്ക് നേടുക.</b>"
    REPLY_TO_DOC_FOR_C2V = "<b>പരിവർത്തനം ചെയ്യാൻ ഒരു ടെലിഗ്രാം മീഡിയയ്ക്ക് മറുപടി നൽകുക.</b>"
    REPLY_TO_DOC_FOR_SCSS = "<b>സ്ക്രീൻഷോട്ടുകൾ ലഭിക്കാൻ ഒരു ടെലിഗ്രാം മീഡിയയ്ക്ക് മറുപടി നൽകുക.</b>"
    SOURCE = """<b>ഹലോ! നിങ്ങൾക്ക് എന്നെ കുറിച്ച് കൂടുതൽ അറിയണോ?</b>

<b>➪ ചാനൽ</b> : <a href="https://t.me/DevAXD">@DevAXD</a>
<b>➪ ഭാഷ :</b> <a href="https://www.python.org/">Python 3.10.5</a>
<b>➪ ശിൽപി :</b> <a href="https://t.me/slogan_98">@slogan_98</a>
<b>➪ പദവി : ചിട്ടി v1</b>"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "<b>ഒരു ടെലിഗ്രാം മീഡിയയ്ക്ക് മറുപടി നൽകുക /rename ഇഷ്‌ടാനുസൃത ലഘുചിത്ര പിന്തുണയോടെ.</b>"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days."
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "<b>ആദ്യം അയക്കു  /downloadmedia ഇതിന്റെ ഒപ്പം ഞാൻ  അത് ലോക്കലായി ഡൌൺലോഡ് ചെയ്യാം . \nഅയക്കുക /Storageinfo മീഡിയ അറിയാൻ, അത് നിലവിൽ ഡൗൺലോഡ് ചെയ്തിരിക്കുന്നു.</b>"
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia To Delete This Media, From My Storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t A Small Photo / Video, From The Above Media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "<b>A Saved Media Already Exists. Please Send /Storageinfo To Know The Current Media Details.</b>"
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "<b>Reply to a Telegram media (MKV), to extract embedded streams.</b>"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "<b>Reply /generatecustomthumbnail to a media album, to generate custom thumbail</b>"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "<b>Media Album Should Contain Only Two Photos. Please Re-send The Media Album, And Then Try Again, Or Send Only Two Photos In An Album.</b>"
    INVALID_UPLOAD_BOT_URL_FORMAT = "<b>URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension</b>"
    ABUSIVE_USERS = "<b>You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction.</b>"
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Holy Shit!!"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice."
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
 users only 1 request per 5 minutes.
/upgrade or Try 300 seconds later."""
    SLOW_URL_DECED = "Gosh That Seems To Be A Very Slow URL. Since You Were Screwing My Home, I Am In No Mood To Download This File. Meanwhile, Why Don't You Get Me A Fast URL So That I can Upload To Telegram, Without Me Slowing Down For Other Users."
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
Please short your file name and try again!"""

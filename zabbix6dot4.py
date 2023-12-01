class  role: 
	roleid                  = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	readonly                = int() #         DEFAULT '0'               NOT NULL,
	
class  users: 
	userid                  = int() #                                    NOT NULL,
	username                = str() #(100)    DEFAULT ''                NOT NULL,
	name                    = str() #(100)    DEFAULT ''                NOT NULL,
	surname                 = str() #(100)    DEFAULT ''                NOT NULL,
	passwd                  = str() #(60)     DEFAULT ''                NOT NULL,
	url                     = str() #(2048)   DEFAULT ''                NOT NULL,
	autologin               = int() #         DEFAULT '0'               NOT NULL,
	autologout              = str() #(32)     DEFAULT '15m'             NOT NULL,
	lang                    = str() #(7)      DEFAULT 'default'         NOT NULL,
	refresh                 = str() #(32)     DEFAULT '30s'             NOT NULL,
	theme                   = str() #(128)    DEFAULT 'default'         NOT NULL,
	attempt_failed          = int() #         DEFAULT 0                 NOT NULL,
	attempt_ip              = str() #(39)     DEFAULT ''                NOT NULL,
	attempt_clock           = int() #         DEFAULT 0                 NOT NULL,
	rows_per_page           = int() #         DEFAULT 50                NOT NULL,
	timezone                = str() #(50)     DEFAULT 'default'         NOT NULL,
	roleid                  = int() #          DEFAULT NULL              NULL,
	userdirectoryid         = int() #          DEFAULT NULL              NULL,
	ts_provisioned          = int() #         DEFAULT '0'               NOT NULL,
	
class  maintenances: 
	maintenanceid           = int() #                                    NOT NULL,
	name                    = str() #(128)    DEFAULT ''                NOT NULL,
	maintenance_type        = int() #         DEFAULT '0'               NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	active_since            = int() #         DEFAULT '0'               NOT NULL,
	active_till             = int() #         DEFAULT '0'               NOT NULL,
	tags_evaltype           = int() #         DEFAULT '0'               NOT NULL,
	
class  hosts: 
	hostid                  = int() #                                    NOT NULL,
	proxy_hostid            = int() #                                    NULL,
	host                    = str() #(128)    DEFAULT ''                NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	ipmi_authtype           = int() #         DEFAULT '-1'              NOT NULL,
	ipmi_privilege          = int() #         DEFAULT '2'               NOT NULL,
	ipmi_username           = str() #(16)     DEFAULT ''                NOT NULL,
	ipmi_password           = str() #(20)     DEFAULT ''                NOT NULL,
	maintenanceid           = int() #                                    NULL,
	maintenance_status      = int() #         DEFAULT '0'               NOT NULL,
	maintenance_type        = int() #         DEFAULT '0'               NOT NULL,
	maintenance_from        = int() #         DEFAULT '0'               NOT NULL,
	name                    = str() #(128)    DEFAULT ''                NOT NULL,
	flags                   = int() #         DEFAULT '0'               NOT NULL,
	templateid              = int() #                                    NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	tls_connect             = int() #         DEFAULT '1'               NOT NULL,
	tls_accept              = int() #         DEFAULT '1'               NOT NULL,
	tls_issuer              = str() #(1024)   DEFAULT ''                NOT NULL,
	tls_subject             = str() #(1024)   DEFAULT ''                NOT NULL,
	tls_psk_identity        = str() #(128)    DEFAULT ''                NOT NULL,
	tls_psk                 = str() #(512)    DEFAULT ''                NOT NULL,
	proxy_address           = str() #(255)    DEFAULT ''                NOT NULL,
	auto_compress           = int() #         DEFAULT '1'               NOT NULL,
	discover                = int() #         DEFAULT '0'               NOT NULL,
	custom_interfaces       = int() #         DEFAULT '0'               NOT NULL,
	uuid                    = str() #(32)     DEFAULT ''                NOT NULL,
	name_upper              = str() #(128)    DEFAULT ''                NOT NULL,
	vendor_name             = str() #(64)     DEFAULT ''                NOT NULL,
	vendor_version          = str() #(32)     DEFAULT ''                NOT NULL,
	
    
class  hstgrp: 
	groupid                 = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	flags                   = int() #         DEFAULT '0'               NOT NULL,
	uuid                    = str() #(32)     DEFAULT ''                NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	
    
class  group_prototype: 
	group_prototypeid       = int() #                                    NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	groupid                 = int() #                                    NULL,
	templateid              = int() #                                    NULL,
	
    
class  group_discovery: 
	groupid                 = int() #                                    NOT NULL,
	parent_group_prototypeid = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	lastcheck               = int() #         DEFAULT '0'               NOT NULL,
	ts_delete               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  drules: 
	druleid                 = int() #                                    NOT NULL,
	proxy_hostid            = int() #                                    NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	iprange                 = str() #(2048)   DEFAULT ''                NOT NULL,
	delay                   = str() #(255)    DEFAULT '1h'              NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	
    
class  dchecks: 
	dcheckid                = int() #                                    NOT NULL,
	druleid                 = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	key_                    = str() #(2048)   DEFAULT ''                NOT NULL,
	snmp_community          = str() #(255)    DEFAULT ''                NOT NULL,
	ports                   = str() #(255)    DEFAULT '0'               NOT NULL,
	snmpv3_securityname     = str() #(64)     DEFAULT ''                NOT NULL,
	snmpv3_securitylevel    = int() #         DEFAULT '0'               NOT NULL,
	snmpv3_authpassphrase   = str() #(64)     DEFAULT ''                NOT NULL,
	snmpv3_privpassphrase   = str() #(64)     DEFAULT ''                NOT NULL,
	uniq                    = int() #         DEFAULT '0'               NOT NULL,
	snmpv3_authprotocol     = int() #         DEFAULT '0'               NOT NULL,
	snmpv3_privprotocol     = int() #         DEFAULT '0'               NOT NULL,
	snmpv3_contextname      = str() #(255)    DEFAULT ''                NOT NULL,
	host_source             = int() #         DEFAULT '1'               NOT NULL,
	name_source             = int() #         DEFAULT '0'               NOT NULL,
	
    
class  httptest: 
	httptestid              = int() #                                    NOT NULL,
	name                    = str() #(64)     DEFAULT ''                NOT NULL,
	delay                   = str() #(255)    DEFAULT '1m'              NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	agent                   = str() #(255)    DEFAULT 'Zabbix'          NOT NULL,
	authentication          = int() #         DEFAULT '0'               NOT NULL,
	http_user               = str() #(64)     DEFAULT ''                NOT NULL,
	http_password           = str() #(64)     DEFAULT ''                NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	templateid              = int() #                                    NULL,
	http_proxy              = str() #(255)    DEFAULT ''                NOT NULL,
	retries                 = int() #         DEFAULT '1'               NOT NULL,
	ssl_cert_file           = str() #(255)    DEFAULT ''                NOT NULL,
	ssl_key_file            = str() #(255)    DEFAULT ''                NOT NULL,
	ssl_key_password        = str() #(64)     DEFAULT ''                NOT NULL,
	verify_peer             = int() #         DEFAULT '0'               NOT NULL,
	verify_host             = int() #         DEFAULT '0'               NOT NULL,
	uuid                    = str() #(32)     DEFAULT ''                NOT NULL,
	
    
class  httpstep: 
	httpstepid              = int() #                                    NOT NULL,
	httptestid              = int() #                                    NOT NULL,
	name                    = str() #(64)     DEFAULT ''                NOT NULL,
	no                      = int() #         DEFAULT '0'               NOT NULL,
	url                     = str() #(2048)   DEFAULT ''                NOT NULL,
	timeout                 = str() #(255)    DEFAULT '15s'             NOT NULL,
	posts                   = str() #            DEFAULT ''                NOT NULL,
	required                = str() #(255)    DEFAULT ''                NOT NULL,
	status_codes            = str() #(255)    DEFAULT ''                NOT NULL,
	follow_redirects        = int() #         DEFAULT '1'               NOT NULL,
	retrieve_mode           = int() #         DEFAULT '0'               NOT NULL,
	post_type               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  interface: 
	interfaceid             = int() #                                    NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	main                    = int() #         DEFAULT '0'               NOT NULL,
	type                    = int() #         DEFAULT '1'               NOT NULL,
	useip                   = int() #         DEFAULT '1'               NOT NULL,
	ip                      = str() #(64)     DEFAULT '127.0.0.1'       NOT NULL,
	dns                     = str() #(255)    DEFAULT ''                NOT NULL,
	port                    = str() #(64)     DEFAULT '10050'           NOT NULL,
	available               = int() #         DEFAULT '0'               NOT NULL,
	error                   = str() #(2048)   DEFAULT ''                NOT NULL,
	errors_from             = int() #         DEFAULT '0'               NOT NULL,
	disable_until           = int() #         DEFAULT '0'               NOT NULL,
	
    
class  valuemap: 
	valuemapid              = int() #                                    NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	name                    = str() #(64)     DEFAULT ''                NOT NULL,
	uuid                    = str() #(32)     DEFAULT ''                NOT NULL,
	
    
class  items: 
	itemid                  = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	snmp_oid                = str() #(512)    DEFAULT ''                NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	key_                    = str() #(2048)   DEFAULT ''                NOT NULL,
	delay                   = str() #(1024)   DEFAULT '0'               NOT NULL,
	history                 = str() #(255)    DEFAULT '90d'             NOT NULL,
	trends                  = str() #(255)    DEFAULT '365d'            NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	value_type              = int() #         DEFAULT '0'               NOT NULL,
	trapper_hosts           = str() #(255)    DEFAULT ''                NOT NULL,
	units                   = str() #(255)    DEFAULT ''                NOT NULL,
	formula                 = str() #(255)    DEFAULT ''                NOT NULL,
	logtimefmt              = str() #(64)     DEFAULT ''                NOT NULL,
	templateid              = int() #                                    NULL,
	valuemapid              = int() #                                    NULL,
	params                  = str() #            DEFAULT ''                NOT NULL,
	ipmi_sensor             = str() #(128)    DEFAULT ''                NOT NULL,
	authtype                = int() #         DEFAULT '0'               NOT NULL,
	username                = str() #(64)     DEFAULT ''                NOT NULL,
	password                = str() #(64)     DEFAULT ''                NOT NULL,
	publickey               = str() #(64)     DEFAULT ''                NOT NULL,
	privatekey              = str() #(64)     DEFAULT ''                NOT NULL,
	flags                   = int() #         DEFAULT '0'               NOT NULL,
	interfaceid             = int() #                                    NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	inventory_link          = int() #         DEFAULT '0'               NOT NULL,
	lifetime                = str() #(255)    DEFAULT '30d'             NOT NULL,
	evaltype                = int() #         DEFAULT '0'               NOT NULL,
	jmx_endpoint            = str() #(255)    DEFAULT ''                NOT NULL,
	master_itemid           = int() #                                    NULL,
	timeout                 = str() #(255)    DEFAULT '3s'              NOT NULL,
	url                     = str() #(2048)   DEFAULT ''                NOT NULL,
	query_fields            = str() #(2048)   DEFAULT ''                NOT NULL,
	posts                   = str() #            DEFAULT ''                NOT NULL,
	status_codes            = str() #(255)    DEFAULT '200'             NOT NULL,
	follow_redirects        = int() #         DEFAULT '1'               NOT NULL,
	post_type               = int() #         DEFAULT '0'               NOT NULL,
	http_proxy              = str() #(255)    DEFAULT ''                NOT NULL,
	headers                 = str() #            DEFAULT ''                NOT NULL,
	retrieve_mode           = int() #         DEFAULT '0'               NOT NULL,
	request_method          = int() #         DEFAULT '0'               NOT NULL,
	output_format           = int() #         DEFAULT '0'               NOT NULL,
	ssl_cert_file           = str() #(255)    DEFAULT ''                NOT NULL,
	ssl_key_file            = str() #(255)    DEFAULT ''                NOT NULL,
	ssl_key_password        = str() #(64)     DEFAULT ''                NOT NULL,
	verify_peer             = int() #         DEFAULT '0'               NOT NULL,
	verify_host             = int() #         DEFAULT '0'               NOT NULL,
	allow_traps             = int() #         DEFAULT '0'               NOT NULL,
	discover                = int() #         DEFAULT '0'               NOT NULL,
	uuid                    = str() #(32)     DEFAULT ''                NOT NULL,
	name_upper              = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  httpstepitem: 
	httpstepitemid          = int() #                                    NOT NULL,
	httpstepid              = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	
    
class  httptestitem: 
	httptestitemid          = int() #                                    NOT NULL,
	httptestid              = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	
    
class  media_type: 
	mediatypeid             = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	name                    = str() #(100)    DEFAULT ''                NOT NULL,
	smtp_server             = str() #(255)    DEFAULT ''                NOT NULL,
	smtp_helo               = str() #(255)    DEFAULT ''                NOT NULL,
	smtp_email              = str() #(255)    DEFAULT ''                NOT NULL,
	exec_path               = str() #(255)    DEFAULT ''                NOT NULL,
	gsm_modem               = str() #(255)    DEFAULT ''                NOT NULL,
	username                = str() #(255)    DEFAULT ''                NOT NULL,
	passwd                  = str() #(255)    DEFAULT ''                NOT NULL,
	status                  = int() #         DEFAULT '1'               NOT NULL,
	smtp_port               = int() #         DEFAULT '25'              NOT NULL,
	smtp_security           = int() #         DEFAULT '0'               NOT NULL,
	smtp_verify_peer        = int() #         DEFAULT '0'               NOT NULL,
	smtp_verify_host        = int() #         DEFAULT '0'               NOT NULL,
	smtp_authentication     = int() #         DEFAULT '0'               NOT NULL,
	maxsessions             = int() #         DEFAULT '1'               NOT NULL,
	maxattempts             = int() #         DEFAULT '3'               NOT NULL,
	attempt_interval        = str() #(32)     DEFAULT '10s'             NOT NULL,
	content_type            = int() #         DEFAULT '1'               NOT NULL,
	script                  = str() #            DEFAULT ''                NOT NULL,
	timeout                 = str() #(32)     DEFAULT '30s'             NOT NULL,
	process_tags            = int() #         DEFAULT '0'               NOT NULL,
	show_event_menu         = int() #         DEFAULT '0'               NOT NULL,
	event_menu_url          = str() #(2048)   DEFAULT ''                NOT NULL,
	event_menu_name         = str() #(255)    DEFAULT ''                NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	provider                = int() #         DEFAULT '0'               NOT NULL,
	
    
class  media_type_param: 
	mediatype_paramid       = int() #                                    NOT NULL,
	mediatypeid             = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(2048)   DEFAULT ''                NOT NULL,
	sortorder               = int() #         DEFAULT '0'               NOT NULL,
	

class  media_type_message: 
	mediatype_messageid     = int() #                                    NOT NULL,
	mediatypeid             = int() #                                    NOT NULL,
	eventsource             = int() #                                   NOT NULL,
	recovery                = int() #                                   NOT NULL,
	subject                 = str() #(255)    DEFAULT ''                NOT NULL,
	message                 = str() #            DEFAULT ''                NOT NULL,
	
    
class  usrgrp: 
	usrgrpid                = int() #                                    NOT NULL,
	name                    = str() #(64)     DEFAULT ''                NOT NULL,
	gui_access              = int() #         DEFAULT '0'               NOT NULL,
	users_status            = int() #         DEFAULT '0'               NOT NULL,
	debug_mode              = int() #         DEFAULT '0'               NOT NULL,
	userdirectoryid         = int() #          DEFAULT NULL              NULL,
	
    
class  users_groups: 
	id                      = int() #                                    NOT NULL,
	usrgrpid                = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	
    
class  scripts: 
	scriptid                = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	command                 = str() #            DEFAULT ''                NOT NULL,
	host_access             = int() #         DEFAULT '2'               NOT NULL,
	usrgrpid                = int() #                                    NULL,
	groupid                 = int() #                                    NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	confirmation            = str() #(255)    DEFAULT ''                NOT NULL,
	type                    = int() #         DEFAULT '5'               NOT NULL,
	execute_on              = int() #         DEFAULT '2'               NOT NULL,
	timeout                 = str() #(32)     DEFAULT '30s'             NOT NULL,
	scope                   = int() #         DEFAULT '1'               NOT NULL,
	port                    = str() #(64)     DEFAULT ''                NOT NULL,
	authtype                = int() #         DEFAULT '0'               NOT NULL,
	username                = str() #(64)     DEFAULT ''                NOT NULL,
	password                = str() #(64)     DEFAULT ''                NOT NULL,
	publickey               = str() #(64)     DEFAULT ''                NOT NULL,
	privatekey              = str() #(64)     DEFAULT ''                NOT NULL,
	menu_path               = str() #(255)    DEFAULT ''                NOT NULL,
	url                     = str() #(2048)   DEFAULT ''                NOT NULL,
	new_window              = int() #         DEFAULT '1'               NOT NULL,
	
    
class  script_param: 
	script_paramid          = int() #                                    NOT NULL,
	scriptid                = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(2048)   DEFAULT ''                NOT NULL,
	
    
class  actions: 
	actionid                = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	eventsource             = int() #         DEFAULT '0'               NOT NULL,
	evaltype                = int() #         DEFAULT '0'               NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	esc_period              = str() #(255)    DEFAULT '1h'              NOT NULL,
	formula                 = str() #(1024)   DEFAULT ''                NOT NULL,
	pause_suppressed        = int() #         DEFAULT '1'               NOT NULL,
	notify_if_canceled      = int() #         DEFAULT '1'               NOT NULL,
	pause_symptoms          = int() #         DEFAULT '1'               NOT NULL,
	
    
class  operations: 
	operationid             = int() #                                    NOT NULL,
	actionid                = int() #                                    NOT NULL,
	operationtype           = int() #         DEFAULT '0'               NOT NULL,
	esc_period              = str() #(255)    DEFAULT '0'               NOT NULL,
	esc_step_from           = int() #         DEFAULT '1'               NOT NULL,
	esc_step_to             = int() #         DEFAULT '1'               NOT NULL,
	evaltype                = int() #         DEFAULT '0'               NOT NULL,
	recovery                = int() #         DEFAULT '0'               NOT NULL,
	
    
class  opmessage: 
	operationid             = int() #                                    NOT NULL,
	default_msg             = int() #         DEFAULT '1'               NOT NULL,
	subject                 = str() #(255)    DEFAULT ''                NOT NULL,
	message                 = str() #            DEFAULT ''                NOT NULL,
	mediatypeid             = int() #                                    NULL,
	
    
class  opmessage_grp: 
	opmessage_grpid         = int() #                                    NOT NULL,
	operationid             = int() #                                    NOT NULL,
	usrgrpid                = int() #                                    NOT NULL,
	
    
class  opmessage_usr: 
	opmessage_usrid         = int() #                                    NOT NULL,
	operationid             = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	
    
class  opcommand: 
	operationid             = int() #                                    NOT NULL,
	scriptid                = int() #                                    NOT NULL,
	
    
class  opcommand_hst: 
	opcommand_hstid         = int() #                                    NOT NULL,
	operationid             = int() #                                    NOT NULL,
	hostid                  = int() #                                    NULL,
	
    
class  opcommand_grp: 
	opcommand_grpid         = int() #                                    NOT NULL,
	operationid             = int() #                                    NOT NULL,
	groupid                 = int() #                                    NOT NULL,
	
    
class  opgroup: 
	opgroupid               = int() #                                    NOT NULL,
	operationid             = int() #                                    NOT NULL,
	groupid                 = int() #                                    NOT NULL,
	
    
class  optemplate: 
	optemplateid            = int() #                                    NOT NULL,
	operationid             = int() #                                    NOT NULL,
	templateid              = int() #                                    NOT NULL,
	
    
class  opconditions: 
	opconditionid           = int() #                                    NOT NULL,
	operationid             = int() #                                    NOT NULL,
	conditiontype           = int() #         DEFAULT '0'               NOT NULL,
	operator                = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  conditions: 
	conditionid             = int() #                                    NOT NULL,
	actionid                = int() #                                    NOT NULL,
	conditiontype           = int() #         DEFAULT '0'               NOT NULL,
	operator                = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	value2                  = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  config: 
	configid                = int() #                                    NOT NULL,
	work_period             = str() #(255)    DEFAULT '1-5,09:00-18:00' NOT NULL,
	alert_usrgrpid          = int() #                                    NULL,
	default_theme           = str() #(128)    DEFAULT 'blue-theme'      NOT NULL,
	authentication_type     = int() #         DEFAULT '0'               NOT NULL,
	discovery_groupid       = int() #                                    NULL,
	max_in_table            = int() #         DEFAULT '50'              NOT NULL,
	search_limit            = int() #         DEFAULT '1000'            NOT NULL,
	severity_color_0        = str() #(6)      DEFAULT '97AAB3'          NOT NULL,
	severity_color_1        = str() #(6)      DEFAULT '7499FF'          NOT NULL,
	severity_color_2        = str() #(6)      DEFAULT 'FFC859'          NOT NULL,
	severity_color_3        = str() #(6)      DEFAULT 'FFA059'          NOT NULL,
	severity_color_4        = str() #(6)      DEFAULT 'E97659'          NOT NULL,
	severity_color_5        = str() #(6)      DEFAULT 'E45959'          NOT NULL,
	severity_name_0         = str() #(32)     DEFAULT 'Not classified'  NOT NULL,
	severity_name_1         = str() #(32)     DEFAULT 'Information'     NOT NULL,
	severity_name_2         = str() #(32)     DEFAULT 'Warning'         NOT NULL,
	severity_name_3         = str() #(32)     DEFAULT 'Average'         NOT NULL,
	severity_name_4         = str() #(32)     DEFAULT 'High'            NOT NULL,
	severity_name_5         = str() #(32)     DEFAULT 'Disaster'        NOT NULL,
	ok_period               = str() #(32)     DEFAULT '5m'              NOT NULL,
	blink_period            = str() #(32)     DEFAULT '2m'              NOT NULL,
	problem_unack_color     = str() #(6)      DEFAULT 'CC0000'          NOT NULL,
	problem_ack_color       = str() #(6)      DEFAULT 'CC0000'          NOT NULL,
	ok_unack_color          = str() #(6)      DEFAULT '009900'          NOT NULL,
	ok_ack_color            = str() #(6)      DEFAULT '009900'          NOT NULL,
	problem_unack_style     = int() #         DEFAULT '1'               NOT NULL,
	problem_ack_style       = int() #         DEFAULT '1'               NOT NULL,
	ok_unack_style          = int() #         DEFAULT '1'               NOT NULL,
	ok_ack_style            = int() #         DEFAULT '1'               NOT NULL,
	snmptrap_logging        = int() #         DEFAULT '1'               NOT NULL,
	server_check_interval   = int() #         DEFAULT '10'              NOT NULL,
	hk_events_mode          = int() #         DEFAULT '1'               NOT NULL,
	hk_events_trigger       = str() #(32)     DEFAULT '365d'            NOT NULL,
	hk_events_internal      = str() #(32)     DEFAULT '1d'              NOT NULL,
	hk_events_discovery     = str() #(32)     DEFAULT '1d'              NOT NULL,
	hk_events_autoreg       = str() #(32)     DEFAULT '1d'              NOT NULL,
	hk_services_mode        = int() #         DEFAULT '1'               NOT NULL,
	hk_services             = str() #(32)     DEFAULT '365d'            NOT NULL,
	hk_audit_mode           = int() #         DEFAULT '1'               NOT NULL,
	hk_audit                = str() #(32)     DEFAULT '365d'            NOT NULL,
	hk_sessions_mode        = int() #         DEFAULT '1'               NOT NULL,
	hk_sessions             = str() #(32)     DEFAULT '365d'            NOT NULL,
	hk_history_mode         = int() #         DEFAULT '1'               NOT NULL,
	hk_history_global       = int() #         DEFAULT '0'               NOT NULL,
	hk_history              = str() #(32)     DEFAULT '90d'             NOT NULL,
	hk_trends_mode          = int() #         DEFAULT '1'               NOT NULL,
	hk_trends_global        = int() #         DEFAULT '0'               NOT NULL,
	hk_trends               = str() #(32)     DEFAULT '365d'            NOT NULL,
	default_inventory_mode  = int() #         DEFAULT '-1'              NOT NULL,
	custom_color            = int() #         DEFAULT '0'               NOT NULL,
	http_auth_enabled       = int() #         DEFAULT '0'               NOT NULL,
	http_login_form         = int() #         DEFAULT '0'               NOT NULL,
	http_strip_domains      = str() #(2048)   DEFAULT ''                NOT NULL,
	http_case_sensitive     = int() #         DEFAULT '1'               NOT NULL,
	ldap_auth_enabled       = int() #         DEFAULT '0'               NOT NULL,
	ldap_case_sensitive     = int() #         DEFAULT '1'               NOT NULL,
	db_extension            = str() #(32)     DEFAULT ''                NOT NULL,
	autoreg_tls_accept      = int() #         DEFAULT '1'               NOT NULL,
	compression_status      = int() #         DEFAULT '0'               NOT NULL,
	compress_older          = str() #(32)     DEFAULT '7d'              NOT NULL,
	instanceid              = str() #(32)     DEFAULT ''                NOT NULL,
	saml_auth_enabled       = int() #         DEFAULT '0'               NOT NULL,
	saml_case_sensitive     = int() #         DEFAULT '0'               NOT NULL,
	default_lang            = str() #(5)      DEFAULT 'en_US'           NOT NULL,
	default_timezone        = str() #(50)     DEFAULT 'system'          NOT NULL,
	login_attempts          = int() #         DEFAULT '5'               NOT NULL,
	login_block             = str() #(32)     DEFAULT '30s'             NOT NULL,
	show_technical_errors   = int() #         DEFAULT '0'               NOT NULL,
	validate_uri_schemes    = int() #         DEFAULT '1'               NOT NULL,
	uri_valid_schemes       = str() #(255)    DEFAULT 'http,https,ftp,file,mailto,tel,ssh' NOT NULL,
	x_frame_options         = str() #(255)    DEFAULT 'SAMEORIGIN'      NOT NULL,
	iframe_sandboxing_enabled = int() #         DEFAULT '1'               NOT NULL,
	iframe_sandboxing_exceptions = str() #(255)    DEFAULT ''                NOT NULL,
	max_overview_table_size = int() #         DEFAULT '50'              NOT NULL,
	history_period          = str() #(32)     DEFAULT '24h'             NOT NULL,
	period_default          = str() #(32)     DEFAULT '1h'              NOT NULL,
	max_period              = str() #(32)     DEFAULT '2y'              NOT NULL,
	socket_timeout          = str() #(32)     DEFAULT '3s'              NOT NULL,
	connect_timeout         = str() #(32)     DEFAULT '3s'              NOT NULL,
	media_type_test_timeout = str() #(32)     DEFAULT '65s'             NOT NULL,
	script_timeout          = str() #(32)     DEFAULT '60s'             NOT NULL,
	item_test_timeout       = str() #(32)     DEFAULT '60s'             NOT NULL,
	session_key             = str() #(32)     DEFAULT ''                NOT NULL,
	url                     = str() #(255)    DEFAULT ''                NOT NULL,
	report_test_timeout     = str() #(32)     DEFAULT '60s'             NOT NULL,
	dbversion_status        = str() #            DEFAULT ''                NOT NULL,
	hk_events_service       = str() #(32)     DEFAULT '1d'              NOT NULL,
	passwd_min_length       = int() #         DEFAULT '8'               NOT NULL,
	passwd_check_rules      = int() #         DEFAULT '8'               NOT NULL,
	auditlog_enabled        = int() #         DEFAULT '1'               NOT NULL,
	ha_failover_delay       = str() #(32)     DEFAULT '1m'              NOT NULL,
	geomaps_tile_provider   = str() #(255)    DEFAULT ''                NOT NULL,
	geomaps_tile_url        = str() #(1024)   DEFAULT ''                NOT NULL,
	geomaps_max_zoom        = int() #         DEFAULT '0'               NOT NULL,
	geomaps_attribution     = str() #(1024)   DEFAULT ''                NOT NULL,
	vault_provider          = int() #         DEFAULT '0'               NOT NULL,
	ldap_userdirectoryid    = int() #          DEFAULT NULL              NULL,
	server_status           = str() #            DEFAULT ''                NOT NULL,
	jit_provision_interval  = str() #(32)     DEFAULT '1h'              NOT NULL,
	saml_jit_status         = int() #         DEFAULT '0'               NOT NULL,
	ldap_jit_status         = int() #         DEFAULT '0'               NOT NULL,
	disabled_usrgrpid       = int() #          DEFAULT NULL              NULL,
	
    
class  triggers: 
	triggerid               = int() #                                    NOT NULL,
	expression              = str() #(2048)   DEFAULT ''                NOT NULL,
	description             = str() #(255)    DEFAULT ''                NOT NULL,
	url                     = str() #(2048)   DEFAULT ''                NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	value                   = int() #         DEFAULT '0'               NOT NULL,
	priority                = int() #         DEFAULT '0'               NOT NULL,
	lastchange              = int() #         DEFAULT '0'               NOT NULL,
	comments                = str() #            DEFAULT ''                NOT NULL,
	error                   = str() #(2048)   DEFAULT ''                NOT NULL,
	templateid              = int() #                                    NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	state                   = int() #         DEFAULT '0'               NOT NULL,
	flags                   = int() #         DEFAULT '0'               NOT NULL,
	recovery_mode           = int() #         DEFAULT '0'               NOT NULL,
	recovery_expression     = str() #(2048)   DEFAULT ''                NOT NULL,
	correlation_mode        = int() #         DEFAULT '0'               NOT NULL,
	correlation_tag         = str() #(255)    DEFAULT ''                NOT NULL,
	manual_close            = int() #         DEFAULT '0'               NOT NULL,
	opdata                  = str() #(255)    DEFAULT ''                NOT NULL,
	discover                = int() #         DEFAULT '0'               NOT NULL,
	event_name              = str() #(2048)   DEFAULT ''                NOT NULL,
	uuid                    = str() #(32)     DEFAULT ''                NOT NULL,
	url_name                = str() #(64)     DEFAULT ''                NOT NULL,
	
    
class  trigger_depends: 
	triggerdepid            = int() #                                    NOT NULL,
	triggerid_down          = int() #                                    NOT NULL,
	triggerid_up            = int() #                                    NOT NULL,
	
    
class  functions: 
	functionid              = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	triggerid               = int() #                                    NOT NULL,
	name                    = str() #(12)     DEFAULT ''                NOT NULL,
	parameter               = str() #(255)    DEFAULT '0'               NOT NULL,
	
    
class  graphs: 
	graphid                 = int() #                                    NOT NULL,
	name                    = str() #(128)    DEFAULT ''                NOT NULL,
	width                   = int() #         DEFAULT '900'             NOT NULL,
	height                  = int() #         DEFAULT '200'             NOT NULL,
	yaxismin                 = int() # '0'               NOT NULL,
	yaxismax                 = int() # '100'             NOT NULL,
	templateid              = int() #                                    NULL,
	show_work_period        = int() #         DEFAULT '1'               NOT NULL,
	show_triggers           = int() #         DEFAULT '1'               NOT NULL,
	graphtype               = int() #         DEFAULT '0'               NOT NULL,
	show_legend             = int() #         DEFAULT '1'               NOT NULL,
	show_3d                 = int() #         DEFAULT '0'               NOT NULL,
	percent_left             = int() # '0'               NOT NULL,
	percent_right            = int() # '0'               NOT NULL,
	ymin_type               = int() #         DEFAULT '0'               NOT NULL,
	ymax_type               = int() #         DEFAULT '0'               NOT NULL,
	ymin_itemid             = int() #                                    NULL,
	ymax_itemid             = int() #                                    NULL,
	flags                   = int() #         DEFAULT '0'               NOT NULL,
	discover                = int() #         DEFAULT '0'               NOT NULL,
	uuid                    = str() #(32)     DEFAULT ''                NOT NULL,
	
    
class  graphs_items: 
	gitemid                 = int() #                                    NOT NULL,
	graphid                 = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	drawtype                = int() #         DEFAULT '0'               NOT NULL,
	sortorder               = int() #         DEFAULT '0'               NOT NULL,
	color                   = str() #(6)      DEFAULT '009600'          NOT NULL,
	yaxisside               = int() #         DEFAULT '0'               NOT NULL,
	calc_fnc                = int() #         DEFAULT '2'               NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,


class  graph_theme: 
	graphthemeid            = int() #                                    NOT NULL,
	theme                   = str() #(64)     DEFAULT ''                NOT NULL,
	backgroundcolor         = str() #(6)      DEFAULT ''                NOT NULL,
	graphcolor              = str() #(6)      DEFAULT ''                NOT NULL,
	gridcolor               = str() #(6)      DEFAULT ''                NOT NULL,
	maingridcolor           = str() #(6)      DEFAULT ''                NOT NULL,
	gridbordercolor         = str() #(6)      DEFAULT ''                NOT NULL,
	textcolor               = str() #(6)      DEFAULT ''                NOT NULL,
	highlightcolor          = str() #(6)      DEFAULT ''                NOT NULL,
	leftpercentilecolor     = str() #(6)      DEFAULT ''                NOT NULL,
	rightpercentilecolor    = str() #(6)      DEFAULT ''                NOT NULL,
	nonworktimecolor        = str() #(6)      DEFAULT ''                NOT NULL,
	colorpalette            = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  globalmacro: 
	globalmacroid           = int() #                                    NOT NULL,
	macro                   = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(2048)   DEFAULT ''                NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	
    
class  hostmacro: 
	hostmacroid             = int() #                                    NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	macro                   = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(2048)   DEFAULT ''                NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	automatic               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  hosts_groups: 
	hostgroupid             = int() #                                    NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	groupid                 = int() #                                    NOT NULL,
	
    
class  hosts_templates: 
	hosttemplateid          = int() #                                    NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	templateid              = int() #                                    NOT NULL,
	link_type               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  valuemap_mapping: 
	valuemap_mappingid      = int() #                                    NOT NULL,
	valuemapid              = int() #                                    NOT NULL,
	value                   = str() #(64)     DEFAULT ''                NOT NULL,
	newvalue                = str() #(64)     DEFAULT ''                NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	sortorder               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  media: 
	mediaid                 = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	mediatypeid             = int() #                                    NOT NULL,
	sendto                  = str() #(1024)   DEFAULT ''                NOT NULL,
	active                  = int() #         DEFAULT '0'               NOT NULL,
	severity                = int() #         DEFAULT '63'              NOT NULL,
	period                  = str() #(1024)   DEFAULT '1-7,00:00-24:00' NOT NULL,
	
    
class  rights: 
	rightid                 = int() #                                    NOT NULL,
	groupid                 = int() #                                    NOT NULL,
	permission              = int() #         DEFAULT '0'               NOT NULL,
	id                      = int() #                                    NOT NULL,
	
    
class  services: 
	serviceid               = int() #                                    NOT NULL,
	name                    = str() #(128)    DEFAULT ''                NOT NULL,
	status                  = int() #         DEFAULT '-1'              NOT NULL,
	algorithm               = int() #         DEFAULT '0'               NOT NULL,
	sortorder               = int() #         DEFAULT '0'               NOT NULL,
	weight                  = int() #         DEFAULT '0'               NOT NULL,
	propagation_rule        = int() #         DEFAULT '0'               NOT NULL,
	propagation_value       = int() #         DEFAULT '0'               NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	uuid                    = str() #(32)     DEFAULT ''                NOT NULL,
	created_at              = int() #         DEFAULT '0'               NOT NULL,
	
    
class  services_links: 
	linkid                  = int() #                                    NOT NULL,
	serviceupid             = int() #                                    NOT NULL,
	servicedownid           = int() #                                    NOT NULL,
	
    
class  icon_map: 
	iconmapid               = int() #                                    NOT NULL,
	name                    = str() #(64)     DEFAULT ''                NOT NULL,
	default_iconid          = int() #                                    NOT NULL,
	
    
class  icon_mapping: 
	iconmappingid           = int() #                                    NOT NULL,
	iconmapid               = int() #                                    NOT NULL,
	iconid                  = int() #                                    NOT NULL,
	inventory_link          = int() #         DEFAULT '0'               NOT NULL,
	expression              = str() #(64)     DEFAULT ''                NOT NULL,
	sortorder               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  sysmaps: 
	sysmapid                = int() #                                    NOT NULL,
	name                    = str() #(128)    DEFAULT ''                NOT NULL,
	width                   = int() #         DEFAULT '600'             NOT NULL,
	height                  = int() #         DEFAULT '400'             NOT NULL,
	backgroundid            = int() #                                    NULL,
	label_type              = int() #         DEFAULT '2'               NOT NULL,
	label_location          = int() #         DEFAULT '0'               NOT NULL,
	highlight               = int() #         DEFAULT '1'               NOT NULL,
	expandproblem           = int() #         DEFAULT '1'               NOT NULL,
	markelements            = int() #         DEFAULT '0'               NOT NULL,
	show_unack              = int() #         DEFAULT '0'               NOT NULL,
	grid_size               = int() #         DEFAULT '50'              NOT NULL,
	grid_show               = int() #         DEFAULT '1'               NOT NULL,
	grid_align              = int() #         DEFAULT '1'               NOT NULL,
	label_format            = int() #         DEFAULT '0'               NOT NULL,
	label_type_host         = int() #         DEFAULT '2'               NOT NULL,
	label_type_hostgroup    = int() #         DEFAULT '2'               NOT NULL,
	label_type_trigger      = int() #         DEFAULT '2'               NOT NULL,
	label_type_map          = int() #         DEFAULT '2'               NOT NULL,
	label_type_image        = int() #         DEFAULT '2'               NOT NULL,
	label_string_host       = str() #(255)    DEFAULT ''                NOT NULL,
	label_string_hostgroup  = str() #(255)    DEFAULT ''                NOT NULL,
	label_string_trigger    = str() #(255)    DEFAULT ''                NOT NULL,
	label_string_map        = str() #(255)    DEFAULT ''                NOT NULL,
	label_string_image      = str() #(255)    DEFAULT ''                NOT NULL,
	iconmapid               = int() #                                    NULL,
	expand_macros           = int() #         DEFAULT '0'               NOT NULL,
	severity_min            = int() #         DEFAULT '0'               NOT NULL,
	userid                  = int() #                                    NOT NULL,
	private                 = int() #         DEFAULT '1'               NOT NULL,
	show_suppressed         = int() #         DEFAULT '0'               NOT NULL,
	
    
class  sysmaps_elements: 
	selementid              = int() #                                    NOT NULL,
	sysmapid                = int() #                                    NOT NULL,
	elementid               = int() #          DEFAULT '0'               NOT NULL,
	elementtype             = int() #         DEFAULT '0'               NOT NULL,
	iconid_off              = int() #                                    NULL,
	iconid_on               = int() #                                    NULL,
	label                   = str() #(2048)   DEFAULT ''                NOT NULL,
	label_location          = int() #         DEFAULT '-1'              NOT NULL,
	x                       = int() #         DEFAULT '0'               NOT NULL,
	y                       = int() #         DEFAULT '0'               NOT NULL,
	iconid_disabled         = int() #                                    NULL,
	iconid_maintenance      = int() #                                    NULL,
	elementsubtype          = int() #         DEFAULT '0'               NOT NULL,
	areatype                = int() #         DEFAULT '0'               NOT NULL,
	width                   = int() #         DEFAULT '200'             NOT NULL,
	height                  = int() #         DEFAULT '200'             NOT NULL,
	viewtype                = int() #         DEFAULT '0'               NOT NULL,
	use_iconmap             = int() #         DEFAULT '1'               NOT NULL,
	evaltype                = int() #         DEFAULT '0'               NOT NULL,
	
    
class  sysmaps_links: 
	linkid                  = int() #                                    NOT NULL,
	sysmapid                = int() #                                    NOT NULL,
	selementid1             = int() #                                    NOT NULL,
	selementid2             = int() #                                    NOT NULL,
	drawtype                = int() #         DEFAULT '0'               NOT NULL,
	color                   = str() #(6)      DEFAULT '000000'          NOT NULL,
	label                   = str() #(2048)   DEFAULT ''                NOT NULL,
	
    
class  sysmaps_link_triggers: 
	linktriggerid           = int() #                                    NOT NULL,
	linkid                  = int() #                                    NOT NULL,
	triggerid               = int() #                                    NOT NULL,
	drawtype                = int() #         DEFAULT '0'               NOT NULL,
	color                   = str() #(6)      DEFAULT '000000'          NOT NULL,
	
    
class  sysmap_element_url: 
	sysmapelementurlid      = int() #                                    NOT NULL,
	selementid              = int() #                                    NOT NULL,
	name                    = str() #(255)                              NOT NULL,
	url                     = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  sysmap_url: 
	sysmapurlid             = int() #                                    NOT NULL,
	sysmapid                = int() #                                    NOT NULL,
	name                    = str() #(255)                              NOT NULL,
	url                     = str() #(255)    DEFAULT ''                NOT NULL,
	elementtype             = int() #         DEFAULT '0'               NOT NULL,
	
    
class  sysmap_user: 
	sysmapuserid            = int() #                                    NOT NULL,
	sysmapid                = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	permission              = int() #         DEFAULT '2'               NOT NULL,
	
    
class  sysmap_usrgrp: 
	sysmapusrgrpid          = int() #                                    NOT NULL,
	sysmapid                = int() #                                    NOT NULL,
	usrgrpid                = int() #                                    NOT NULL,
	permission              = int() #         DEFAULT '2'               NOT NULL,


class  maintenances_hosts: 
	maintenance_hostid      = int() #                                    NOT NULL,
	maintenanceid           = int() #                                    NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	
    
class  maintenances_groups: 
	maintenance_groupid     = int() #                                    NOT NULL,
	maintenanceid           = int() #                                    NOT NULL,
	groupid                 = int() #                                    NOT NULL,
	
    
class  timeperiods: 
	timeperiodid            = int() #                                    NOT NULL,
	timeperiod_type         = int() #         DEFAULT '0'               NOT NULL,
	every                   = int() #         DEFAULT '1'               NOT NULL,
	month                   = int() #         DEFAULT '0'               NOT NULL,
	dayofweek               = int() #         DEFAULT '0'               NOT NULL,
	day                     = int() #         DEFAULT '0'               NOT NULL,
	start_time              = int() #         DEFAULT '0'               NOT NULL,
	period                  = int() #         DEFAULT '0'               NOT NULL,
	start_date              = int() #         DEFAULT '0'               NOT NULL,
	
    
class  maintenances_windows: 
	maintenance_timeperiodid = int() #                                    NOT NULL,
	maintenanceid           = int() #                                    NOT NULL,
	timeperiodid            = int() #                                    NOT NULL,
	
    
class  regexps: 
	regexpid                = int() #                                    NOT NULL,
	name                    = str() #(128)    DEFAULT ''                NOT NULL,
	test_string             = str() #            DEFAULT ''                NOT NULL,
	
    
class  expressions: 
	expressionid            = int() #                                    NOT NULL,
	regexpid                = int() #                                    NOT NULL,
	expression              = str() #(255)    DEFAULT ''                NOT NULL,
	expression_type         = int() #         DEFAULT '0'               NOT NULL,
	exp_delimiter           = str() #(1)      DEFAULT ''                NOT NULL,
	case_sensitive          = int() #         DEFAULT '0'               NOT NULL,
	
    
class  ids: 
	table_name              = str() #(64)     DEFAULT ''                NOT NULL,
	field_name              = str() #(64)     DEFAULT ''                NOT NULL,
	nextid                  = int() #                                    NOT NULL,
	
    
class  alerts: 
	alertid                 = int() #                                    NOT NULL,
	actionid                = int() #                                    NOT NULL,
	eventid                 = int() #                                    NOT NULL,
	userid                  = int() #                                    NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	mediatypeid             = int() #                                    NULL,
	sendto                  = str() #(1024)   DEFAULT ''                NOT NULL,
	subject                 = str() #(255)    DEFAULT ''                NOT NULL,
	message                 = str() #            DEFAULT ''                NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	retries                 = int() #         DEFAULT '0'               NOT NULL,
	error                   = str() #(2048)   DEFAULT ''                NOT NULL,
	esc_step                = int() #         DEFAULT '0'               NOT NULL,
	alerttype               = int() #         DEFAULT '0'               NOT NULL,
	p_eventid               = int() #                                    NULL,
	acknowledgeid           = int() #                                    NULL,
	parameters              = str() #            DEFAULT '{}'              NOT NULL,
	
    
class  history: 
	itemid                  = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	value                    = int() # '0.0000'          NOT NULL,
	ns                      = int() #         DEFAULT '0'               NOT NULL,


class  history_uint: 
	itemid                  = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	value                    = int() #(20)     DEFAULT '0'               NOT NULL,
	ns                      = int() #         DEFAULT '0'               NOT NULL,
	
    
class  history_str: 
	itemid                  = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	ns                      = int() #         DEFAULT '0'               NOT NULL,
	
    
class  history_log: 
	itemid                  = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	timestamp               = int() #         DEFAULT '0'               NOT NULL,
	source                  = str() #(64)     DEFAULT ''                NOT NULL,
	severity                = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #            DEFAULT ''                NOT NULL,
	logeventid              = int() #         DEFAULT '0'               NOT NULL,
	ns                      = int() #         DEFAULT '0'               NOT NULL,
	
    
class  history_text: 
	itemid                  = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #            DEFAULT ''                NOT NULL,
	ns                      = int() #         DEFAULT '0'               NOT NULL,
	
    
class  proxy_history: 
	id                       = int() #                                 NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	timestamp               = int() #         DEFAULT '0'               NOT NULL,
	source                  = str() #(64)     DEFAULT ''                NOT NULL,
	severity                = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #            DEFAULT ''                NOT NULL,
	logeventid              = int() #         DEFAULT '0'               NOT NULL,
	ns                      = int() #         DEFAULT '0'               NOT NULL,
	state                   = int() #         DEFAULT '0'               NOT NULL,
	lastlogsize              = int() #(20)     DEFAULT '0'               NOT NULL,
	mtime                   = int() #         DEFAULT '0'               NOT NULL,
	flags                   = int() #         DEFAULT '0'               NOT NULL,
	write_clock             = int() #         DEFAULT '0'               NOT NULL,
	
    
    
class  proxy_dhistory: 
	id                       = int() #                                 NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	druleid                 = int() #                                    NOT NULL,
	ip                      = str() #(39)     DEFAULT ''                NOT NULL,
	port                    = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	dcheckid                = int() #                                    NULL,
	dns                     = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  events: 
	eventid                 = int() #                                    NOT NULL,
	source                  = int() #         DEFAULT '0'               NOT NULL,
	object                  = int() #         DEFAULT '0'               NOT NULL,
	objectid                = int() #          DEFAULT '0'               NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	value                   = int() #         DEFAULT '0'               NOT NULL,
	acknowledged            = int() #         DEFAULT '0'               NOT NULL,
	ns                      = int() #         DEFAULT '0'               NOT NULL,
	name                    = str() #(2048)   DEFAULT ''                NOT NULL,
	severity                = int() #         DEFAULT '0'               NOT NULL,


class  event_symptom: 
	eventid                 = int() #                                    NOT NULL,
	cause_eventid           = int() #                                    NOT NULL,
	
    
class  trends: 
	itemid                  = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	num                     = int() #         DEFAULT '0'               NOT NULL,
	value_min                = int() # '0.0000'          NOT NULL,
	value_avg                = int() # '0.0000'          NOT NULL,
	value_max                = int() # '0.0000'          NOT NULL,
	
    
class  trends_uint: 
	itemid                  = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	num                     = int() #         DEFAULT '0'               NOT NULL,
	value_min                = int() #(20)     DEFAULT '0'               NOT NULL,
	value_avg                = int() #(20)     DEFAULT '0'               NOT NULL,
	value_max                = int() #(20)     DEFAULT '0'               NOT NULL,
	
    
class  acknowledges: 
	acknowledgeid           = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	eventid                 = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	message                 = str() #(2048)   DEFAULT ''                NOT NULL,
	action                  = int() #         DEFAULT '0'               NOT NULL,
	old_severity            = int() #         DEFAULT '0'               NOT NULL,
	new_severity            = int() #         DEFAULT '0'               NOT NULL,
	suppress_until          = int() #         DEFAULT '0'               NOT NULL,
	taskid                  = int() #                                    NULL,
	
    
class  auditlog: 
	auditid                 = str() #(25)                               NOT NULL,
	userid                  = int() #                                    NULL,
	username                = str() #(100)    DEFAULT ''                NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	ip                      = str() #(39)     DEFAULT ''                NOT NULL,
	action                  = int() #         DEFAULT '0'               NOT NULL,
	resourcetype            = int() #         DEFAULT '0'               NOT NULL,
	resourceid              = int() #                                    NULL,
	resource_cuid           = str() #(25)                               NULL,
	resourcename            = str() #(255)    DEFAULT ''                NOT NULL,
	recordsetid             = str() #(25)                               NOT NULL,
	details                 = str() #            DEFAULT ''                NOT NULL,
	
    
class  service_alarms: 
	servicealarmid          = int() #                                    NOT NULL,
	serviceid               = int() #                                    NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	value                   = int() #         DEFAULT '-1'              NOT NULL,
	
    
class  autoreg_host: 
	autoreg_hostid          = int() #                                    NOT NULL,
	proxy_hostid            = int() #                                    NULL,
	host                    = str() #(128)    DEFAULT ''                NOT NULL,
	listen_ip               = str() #(39)     DEFAULT ''                NOT NULL,
	listen_port             = int() #         DEFAULT '0'               NOT NULL,
	listen_dns              = str() #(255)    DEFAULT ''                NOT NULL,
	host_metadata           = str() #            DEFAULT ''                NOT NULL,
	flags                   = int() #         DEFAULT '0'               NOT NULL,
	tls_accepted            = int() #         DEFAULT '1'               NOT NULL,
	
    
class  proxy_autoreg_host: 
	id                       = int() #                                 NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	host                    = str() #(128)    DEFAULT ''                NOT NULL,
	listen_ip               = str() #(39)     DEFAULT ''                NOT NULL,
	listen_port             = int() #         DEFAULT '0'               NOT NULL,
	listen_dns              = str() #(255)    DEFAULT ''                NOT NULL,
	host_metadata           = str() #            DEFAULT ''                NOT NULL,
	flags                   = int() #         DEFAULT '0'               NOT NULL,
	tls_accepted            = int() #         DEFAULT '1'               NOT NULL,
	
    
class  dhosts: 
	dhostid                 = int() #                                    NOT NULL,
	druleid                 = int() #                                    NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	lastup                  = int() #         DEFAULT '0'               NOT NULL,
	lastdown                = int() #         DEFAULT '0'               NOT NULL,
	dcheckid                = int() #                                    NOT NULL,
	ip                      = str() #(39)     DEFAULT ''                NOT NULL,
	dns                     = str() #(255)    DEFAULT ''                NOT NULL,
	
class  dservices: 
	dserviceid              = int() #                                    NOT NULL,
	dhostid                 = int() #                                    NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	port                    = int() #         DEFAULT '0'               NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	lastup                  = int() #         DEFAULT '0'               NOT NULL,
	lastdown                = int() #         DEFAULT '0'               NOT NULL,
	dcheckid                = int() #                                    NOT NULL,
	ip                      = str() #(39)     DEFAULT ''                NOT NULL,
	dns                     = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  escalations: 
	escalationid            = int() #                                    NOT NULL,
	actionid                = int() #                                    NOT NULL,
	triggerid               = int() #                                    NULL,
	eventid                 = int() #                                    NULL,
	r_eventid               = int() #                                    NULL,
	nextcheck               = int() #         DEFAULT '0'               NOT NULL,
	esc_step                = int() #         DEFAULT '0'               NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	itemid                  = int() #                                    NULL,
	acknowledgeid           = int() #                                    NULL,
	servicealarmid          = int() #                                    NULL,
	serviceid               = int() #                                    NULL,
	
    
class  globalvars: 
	globalvarid             = int() #                                    NOT NULL,
	snmp_lastsize            = int() #(20)     DEFAULT '0'               NOT NULL,
	
    
class  graph_discovery: 
	graphid                 = int() #                                    NOT NULL,
	parent_graphid          = int() #                                    NOT NULL,
	lastcheck               = int() #         DEFAULT '0'               NOT NULL,
	ts_delete               = int() #         DEFAULT '0'               NOT NULL,


class  host_inventory: 
	hostid                  = int() #                                    NOT NULL,
	inventory_mode          = int() #         DEFAULT '0'               NOT NULL,
	type                    = str() #(64)     DEFAULT ''                NOT NULL,
	type_full               = str() #(64)     DEFAULT ''                NOT NULL,
	name                    = str() #(128)    DEFAULT ''                NOT NULL,
	alias                   = str() #(128)    DEFAULT ''                NOT NULL,
	os                      = str() #(128)    DEFAULT ''                NOT NULL,
	os_full                 = str() #(255)    DEFAULT ''                NOT NULL,
	os_short                = str() #(128)    DEFAULT ''                NOT NULL,
	serialno_a              = str() #(64)     DEFAULT ''                NOT NULL,
	serialno_b              = str() #(64)     DEFAULT ''                NOT NULL,
	tag                     = str() #(64)     DEFAULT ''                NOT NULL,
	asset_tag               = str() #(64)     DEFAULT ''                NOT NULL,
	macaddress_a            = str() #(64)     DEFAULT ''                NOT NULL,
	macaddress_b            = str() #(64)     DEFAULT ''                NOT NULL,
	hardware                = str() #(255)    DEFAULT ''                NOT NULL,
	hardware_full           = str() #            DEFAULT ''                NOT NULL,
	software                = str() #(255)    DEFAULT ''                NOT NULL,
	software_full           = str() #            DEFAULT ''                NOT NULL,
	software_app_a          = str() #(64)     DEFAULT ''                NOT NULL,
	software_app_b          = str() #(64)     DEFAULT ''                NOT NULL,
	software_app_c          = str() #(64)     DEFAULT ''                NOT NULL,
	software_app_d          = str() #(64)     DEFAULT ''                NOT NULL,
	software_app_e          = str() #(64)     DEFAULT ''                NOT NULL,
	contact                 = str() #            DEFAULT ''                NOT NULL,
	location                = str() #            DEFAULT ''                NOT NULL,
	location_lat            = str() #(16)     DEFAULT ''                NOT NULL,
	location_lon            = str() #(16)     DEFAULT ''                NOT NULL,
	notes                   = str() #            DEFAULT ''                NOT NULL,
	chassis                 = str() #(64)     DEFAULT ''                NOT NULL,
	model                   = str() #(64)     DEFAULT ''                NOT NULL,
	hw_arch                 = str() #(32)     DEFAULT ''                NOT NULL,
	vendor                  = str() #(64)     DEFAULT ''                NOT NULL,
	contract_number         = str() #(64)     DEFAULT ''                NOT NULL,
	installer_name          = str() #(64)     DEFAULT ''                NOT NULL,
	deployment_status       = str() #(64)     DEFAULT ''                NOT NULL,
	url_a                   = str() #(255)    DEFAULT ''                NOT NULL,
	url_b                   = str() #(255)    DEFAULT ''                NOT NULL,
	url_c                   = str() #(255)    DEFAULT ''                NOT NULL,
	host_networks           = str() #            DEFAULT ''                NOT NULL,
	host_netmask            = str() #(39)     DEFAULT ''                NOT NULL,
	host_router             = str() #(39)     DEFAULT ''                NOT NULL,
	oob_ip                  = str() #(39)     DEFAULT ''                NOT NULL,
	oob_netmask             = str() #(39)     DEFAULT ''                NOT NULL,
	oob_router              = str() #(39)     DEFAULT ''                NOT NULL,
	date_hw_purchase        = str() #(64)     DEFAULT ''                NOT NULL,
	date_hw_install         = str() #(64)     DEFAULT ''                NOT NULL,
	date_hw_expiry          = str() #(64)     DEFAULT ''                NOT NULL,
	date_hw_decomm          = str() #(64)     DEFAULT ''                NOT NULL,
	site_address_a          = str() #(128)    DEFAULT ''                NOT NULL,
	site_address_b          = str() #(128)    DEFAULT ''                NOT NULL,
	site_address_c          = str() #(128)    DEFAULT ''                NOT NULL,
	site_city               = str() #(128)    DEFAULT ''                NOT NULL,
	site_state              = str() #(64)     DEFAULT ''                NOT NULL,
	site_country            = str() #(64)     DEFAULT ''                NOT NULL,
	site_zip                = str() #(64)     DEFAULT ''                NOT NULL,
	site_rack               = str() #(128)    DEFAULT ''                NOT NULL,
	site_notes              = str() #            DEFAULT ''                NOT NULL,
	poc_1_name              = str() #(128)    DEFAULT ''                NOT NULL,
	poc_1_email             = str() #(128)    DEFAULT ''                NOT NULL,
	poc_1_phone_a           = str() #(64)     DEFAULT ''                NOT NULL,
	poc_1_phone_b           = str() #(64)     DEFAULT ''                NOT NULL,
	poc_1_cell              = str() #(64)     DEFAULT ''                NOT NULL,
	poc_1_screen            = str() #(64)     DEFAULT ''                NOT NULL,
	poc_1_notes             = str() #            DEFAULT ''                NOT NULL,
	poc_2_name              = str() #(128)    DEFAULT ''                NOT NULL,
	poc_2_email             = str() #(128)    DEFAULT ''                NOT NULL,
	poc_2_phone_a           = str() #(64)     DEFAULT ''                NOT NULL,
	poc_2_phone_b           = str() #(64)     DEFAULT ''                NOT NULL,
	poc_2_cell              = str() #(64)     DEFAULT ''                NOT NULL,
	poc_2_screen            = str() #(64)     DEFAULT ''                NOT NULL,
	poc_2_notes             = str() #            DEFAULT ''                NOT NULL,
	
    
class  housekeeper: 
	housekeeperid           = int() #                                    NOT NULL,
	tablename               = str() #(64)     DEFAULT ''                NOT NULL,
	field                   = str() #(64)     DEFAULT ''                NOT NULL,
	value                   = int() #                                    NOT NULL,
	
    
class  images: 
	imageid                 = int() #                                    NOT NULL,
	imagetype               = int() #         DEFAULT '0'               NOT NULL,
	name                    = str() #(64)     DEFAULT '0'               NOT NULL,
	image                   = bytes() #           DEFAULT ''                NOT NULL,
	
    
class  item_discovery: 
	itemdiscoveryid         = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	parent_itemid           = int() #                                    NOT NULL,
	key_                    = str() #(2048)   DEFAULT ''                NOT NULL,
	lastcheck               = int() #         DEFAULT '0'               NOT NULL,
	ts_delete               = int() #         DEFAULT '0'               NOT NULL,


class  host_discovery: 
	hostid                  = int() #                                    NOT NULL,
	parent_hostid           = int() #                                    NULL,
	parent_itemid           = int() #                                    NULL,
	host                    = str() #(128)    DEFAULT ''                NOT NULL,
	lastcheck               = int() #         DEFAULT '0'               NOT NULL,
	ts_delete               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  interface_discovery: 
	interfaceid             = int() #                                    NOT NULL,
	parent_interfaceid      = int() #                                    NOT NULL,
	
    
class  profiles: 
	profileid               = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	idx                     = str() #(96)     DEFAULT ''                NOT NULL,
	idx2                    = int() #          DEFAULT '0'               NOT NULL,
	value_id                = int() #          DEFAULT '0'               NOT NULL,
	value_int               = int() #         DEFAULT '0'               NOT NULL,
	value_str               = str() #            DEFAULT ''                NOT NULL,
	source                  = str() #(96)     DEFAULT ''                NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	
    
class  sessions: 
	sessionid               = str() #(32)     DEFAULT ''                NOT NULL,
	userid                  = int() #                                    NOT NULL,
	lastaccess              = int() #         DEFAULT '0'               NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	secret                  = str() #(32)     DEFAULT ''                NOT NULL,
	
    
class  trigger_discovery: 
	triggerid               = int() #                                    NOT NULL,
	parent_triggerid        = int() #                                    NOT NULL,
	lastcheck               = int() #         DEFAULT '0'               NOT NULL,
	ts_delete               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  item_condition: 
	item_conditionid        = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	operator                = int() #         DEFAULT '8'               NOT NULL,
	macro                   = str() #(64)     DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
class  item_rtdata: 
	itemid                  = int() #                                    NOT NULL,
	lastlogsize              = int() #(20)     DEFAULT '0'               NOT NULL,
	state                   = int() #         DEFAULT '0'               NOT NULL,
	mtime                   = int() #         DEFAULT '0'               NOT NULL,
	error                   = str() #(2048)   DEFAULT ''                NOT NULL,
	
class  opinventory: 
	operationid             = int() #                                    NOT NULL,
	inventory_mode          = int() #         DEFAULT '0'               NOT NULL,
	
class  trigger_tag: 
	triggertagid            = int() #                                    NOT NULL,
	triggerid               = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
class  event_tag: 
	eventtagid              = int() #                                    NOT NULL,
	eventid                 = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
class  problem: 
	eventid                 = int() #                                    NOT NULL,
	source                  = int() #         DEFAULT '0'               NOT NULL,
	object                  = int() #         DEFAULT '0'               NOT NULL,
	objectid                = int() #          DEFAULT '0'               NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	ns                      = int() #         DEFAULT '0'               NOT NULL,
	r_eventid               = int() #                                    NULL,
	r_clock                 = int() #         DEFAULT '0'               NOT NULL,
	r_ns                    = int() #         DEFAULT '0'               NOT NULL,
	correlationid           = int() #                                    NULL,
	userid                  = int() #                                    NULL,
	name                    = str() #(2048)   DEFAULT ''                NOT NULL,
	acknowledged            = int() #         DEFAULT '0'               NOT NULL,
	severity                = int() #         DEFAULT '0'               NOT NULL,
	cause_eventid           = int() #                                    NULL,
	
class  problem_tag: 
	problemtagid            = int() #                                    NOT NULL,
	eventid                 = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
class  tag_filter: 
	tag_filterid            = int() #                                    NOT NULL,
	usrgrpid                = int() #                                    NOT NULL,
	groupid                 = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
class  event_recovery: 
	eventid                 = int() #                                    NOT NULL,
	r_eventid               = int() #                                    NOT NULL,
	c_eventid               = int() #                                    NULL,
	correlationid           = int() #                                    NULL,
	userid                  = int() #                                    NULL,
	
class  correlation: 
	correlationid           = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	evaltype                = int() #         DEFAULT '0'               NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	formula                 = str() #(255)    DEFAULT ''                NOT NULL,
	
class  corr_condition: 
	corr_conditionid        = int() #                                    NOT NULL,
	correlationid           = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	
class  corr_condition_tag: 
	corr_conditionid        = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	
class  corr_condition_group: 
	corr_conditionid        = int() #                                    NOT NULL,
	operator                = int() #         DEFAULT '0'               NOT NULL,
	groupid                 = int() #                                    NOT NULL,

class  corr_condition_tagpair: 
	corr_conditionid        = int() #                                    NOT NULL,
	oldtag                  = str() #(255)    DEFAULT ''                NOT NULL,
	newtag                  = str() #(255)    DEFAULT ''                NOT NULL,
	
class  corr_condition_tagvalue: 
	corr_conditionid        = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	operator                = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
class  corr_operation: 
	corr_operationid        = int() #                                    NOT NULL,
	correlationid           = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	
class  task: 
	taskid                  = int() #                                    NOT NULL,
	type                    = int() #                                   NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	ttl                     = int() #         DEFAULT '0'               NOT NULL,
	proxy_hostid            = int() #                                    NULL,
	
class  task_close_problem: 
	taskid                  = int() #                                    NOT NULL,
	acknowledgeid           = int() #                                    NOT NULL,
	
class  item_preproc: 
	item_preprocid          = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	step                    = int() #         DEFAULT '0'               NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	params                  = str() #            DEFAULT ''                NOT NULL,
	error_handler           = int() #         DEFAULT '0'               NOT NULL,
	error_handler_params    = str() #(255)    DEFAULT ''                NOT NULL,
	
class  task_remote_command: 
	taskid                  = int() #                                    NOT NULL,
	command_type            = int() #         DEFAULT '0'               NOT NULL,
	execute_on              = int() #         DEFAULT '0'               NOT NULL,
	port                    = int() #         DEFAULT '0'               NOT NULL,
	authtype                = int() #         DEFAULT '0'               NOT NULL,
	username                = str() #(64)     DEFAULT ''                NOT NULL,
	password                = str() #(64)     DEFAULT ''                NOT NULL,
	publickey               = str() #(64)     DEFAULT ''                NOT NULL,
	privatekey              = str() #(64)     DEFAULT ''                NOT NULL,
	command                 = str() #            DEFAULT ''                NOT NULL,
	alertid                 = int() #                                    NULL,
	parent_taskid           = int() #                                    NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	
class  task_remote_command_result: 
	taskid                  = int() #                                    NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	parent_taskid           = int() #                                    NOT NULL,
	info                    = str() #            DEFAULT ''                NOT NULL,
	
    
class  task_data: 
	taskid                  = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	data                    = str() #            DEFAULT ''                NOT NULL,
	parent_taskid           = int() #                                    NULL,
	
    
class  task_result: 
	taskid                  = int() #                                    NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	parent_taskid           = int() #                                    NOT NULL,
	info                    = str() #            DEFAULT ''                NOT NULL,
	
    
    
class  task_acknowledge: 
	taskid                  = int() #                                    NOT NULL,
	acknowledgeid           = int() #                                    NOT NULL,
	
    
class  sysmap_shape: 
	sysmap_shapeid          = int() #                                    NOT NULL,
	sysmapid                = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	x                       = int() #         DEFAULT '0'               NOT NULL,
	y                       = int() #         DEFAULT '0'               NOT NULL,
	width                   = int() #         DEFAULT '200'             NOT NULL,
	height                  = int() #         DEFAULT '200'             NOT NULL,
	text                    = str() #            DEFAULT ''                NOT NULL,
	font                    = int() #         DEFAULT '9'               NOT NULL,
	font_size               = int() #         DEFAULT '11'              NOT NULL,
	font_color              = str() #(6)      DEFAULT '000000'          NOT NULL,
	text_halign             = int() #         DEFAULT '0'               NOT NULL,
	text_valign             = int() #         DEFAULT '0'               NOT NULL,
	border_type             = int() #         DEFAULT '0'               NOT NULL,
	border_width            = int() #         DEFAULT '1'               NOT NULL,
	border_color            = str() #(6)      DEFAULT '000000'          NOT NULL,
	background_color        = str() #(6)      DEFAULT ''                NOT NULL,
	zindex                  = int() #         DEFAULT '0'               NOT NULL,
	
    
class  sysmap_element_trigger: 
	selement_triggerid      = int() #                                    NOT NULL,
	selementid              = int() #                                    NOT NULL,
	triggerid               = int() #                                    NOT NULL,
	
    
class  httptest_field: 
	httptest_fieldid        = int() #                                    NOT NULL,
	httptestid              = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #            DEFAULT ''                NOT NULL,
	
    
class  httpstep_field: 
	httpstep_fieldid        = int() #                                    NOT NULL,
	httpstepid              = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #            DEFAULT ''                NOT NULL,
	
    
class  dashboard: 
	dashboardid             = int() #                                    NOT NULL,
	name                    = str() #(255)                              NOT NULL,
	userid                  = int() #                                    NULL,
	private                 = int() #         DEFAULT '1'               NOT NULL,
	templateid              = int() #                                    NULL,
	display_period          = int() #         DEFAULT '30'              NOT NULL,
	auto_start              = int() #         DEFAULT '1'               NOT NULL,
	uuid                    = str() #(32)     DEFAULT ''                NOT NULL,
	
    
class  dashboard_user: 
	dashboard_userid        = int() #                                    NOT NULL,
	dashboardid             = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	permission              = int() #         DEFAULT '2'               NOT NULL,
	
    
class  dashboard_usrgrp: 
	dashboard_usrgrpid      = int() #                                    NOT NULL,
	dashboardid             = int() #                                    NOT NULL,
	usrgrpid                = int() #                                    NOT NULL,
	permission              = int() #         DEFAULT '2'               NOT NULL,
	
    
class  dashboard_page: 
	dashboard_pageid        = int() #                                    NOT NULL,
	dashboardid             = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	display_period          = int() #         DEFAULT '0'               NOT NULL,
	sortorder               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  widget: 
	widgetid                = int() #                                    NOT NULL,
	type                    = str() #(255)    DEFAULT ''                NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	x                       = int() #         DEFAULT '0'               NOT NULL,
	y                       = int() #         DEFAULT '0'               NOT NULL,
	width                   = int() #         DEFAULT '1'               NOT NULL,
	height                  = int() #         DEFAULT '2'               NOT NULL,
	view_mode               = int() #         DEFAULT '0'               NOT NULL,
	dashboard_pageid        = int() #                                    NOT NULL,
	
    
class  widget_field: 
	widget_fieldid          = int() #                                    NOT NULL,
	widgetid                = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	value_int               = int() #         DEFAULT '0'               NOT NULL,
	value_str               = str() #(255)    DEFAULT ''                NOT NULL,
	value_groupid           = int() #                                    NULL,
	value_hostid            = int() #                                    NULL,
	value_itemid            = int() #                                    NULL,
	value_graphid           = int() #                                    NULL,
	value_sysmapid          = int() #                                    NULL,
	value_serviceid         = int() #                                    NULL,
	value_slaid             = int() #                                    NULL,
	value_userid            = int() #                                    NULL,
	value_actionid          = int() #                                    NULL,
	value_mediatypeid       = int() #                                    NULL,
	
    
class  task_check_now: 
	taskid                  = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	
    
class  event_suppress: 
	event_suppressid        = int() #                                    NOT NULL,
	eventid                 = int() #                                    NOT NULL,
	maintenanceid           = int() #                                    NULL,
	suppress_until          = int() #         DEFAULT '0'               NOT NULL,
	userid                  = int() #                                    NULL,
	
    
class  maintenance_tag: 
	maintenancetagid        = int() #                                    NOT NULL,
	maintenanceid           = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	operator                = int() #         DEFAULT '2'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  lld_macro_path: 
	lld_macro_pathid        = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	lld_macro               = str() #(255)    DEFAULT ''                NOT NULL,
	path                    = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  host_tag: 
	hosttagid               = int() #                                    NOT NULL,
	hostid                  = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	automatic               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  config_autoreg_tls: 
	autoreg_tlsid           = int() #                                    NOT NULL,
	tls_psk_identity        = str() #(128)    DEFAULT ''                NOT NULL,
	tls_psk                 = str() #(512)    DEFAULT ''                NOT NULL,
	
    
class  module: 
	moduleid                = int() #                                    NOT NULL,
	id                      = str() #(255)    DEFAULT ''                NOT NULL,
	relative_path           = str() #(255)    DEFAULT ''                NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	config                  = str() #            DEFAULT ''                NOT NULL,
	
    
class  interface_snmp: 
	interfaceid             = int() #                                    NOT NULL,
	version                 = int() #         DEFAULT '2'               NOT NULL,
	bulk                    = int() #         DEFAULT '1'               NOT NULL,
	community               = str() #(64)     DEFAULT ''                NOT NULL,
	securityname            = str() #(64)     DEFAULT ''                NOT NULL,
	securitylevel           = int() #         DEFAULT '0'               NOT NULL,
	authpassphrase          = str() #(64)     DEFAULT ''                NOT NULL,
	privpassphrase          = str() #(64)     DEFAULT ''                NOT NULL,
	authprotocol            = int() #         DEFAULT '0'               NOT NULL,
	privprotocol            = int() #         DEFAULT '0'               NOT NULL,
	contextname             = str() #(255)    DEFAULT ''                NOT NULL,
	max_repetitions         = int() #         DEFAULT '10'              NOT NULL,
	
    
class  lld_override: 
	lld_overrideid          = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	step                    = int() #         DEFAULT '0'               NOT NULL,
	evaltype                = int() #         DEFAULT '0'               NOT NULL,
	formula                 = str() #(255)    DEFAULT ''                NOT NULL,
	stop                    = int() #         DEFAULT '0'               NOT NULL,
	
    
class  lld_override_condition: 
	lld_override_conditionid = int() #                                    NOT NULL,
	lld_overrideid          = int() #                                    NOT NULL,
	operator                = int() #         DEFAULT '8'               NOT NULL,
	macro                   = str() #(64)     DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
    
class  lld_override_operation: 
	lld_override_operationid = int() #                                    NOT NULL,
	lld_overrideid          = int() #                                    NOT NULL,
	operationobject         = int() #         DEFAULT '0'               NOT NULL,
	operator                = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  lld_override_opstatus: 
	lld_override_operationid = int() #                                    NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	
    
class  lld_override_opdiscover: 
	lld_override_operationid = int() #                                    NOT NULL,
	discover                = int() #         DEFAULT '0'               NOT NULL,
	
    
class  lld_override_opperiod: 
	lld_override_operationid = int() #                                    NOT NULL,
	delay                   = str() #(1024)   DEFAULT '0'               NOT NULL,
	
    
class  lld_override_ophistory: 
	lld_override_operationid = int() #                                    NOT NULL,
	history                 = str() #(255)    DEFAULT '90d'             NOT NULL,
	
    
class  lld_override_optrends: 
	lld_override_operationid = int() #                                    NOT NULL,
	trends                  = str() #(255)    DEFAULT '365d'            NOT NULL,
	
    
class  lld_override_opseverity: 
	lld_override_operationid = int() #                                    NOT NULL,
	severity                = int() #         DEFAULT '0'               NOT NULL,
	
    
class  lld_override_optag: 
	lld_override_optagid    = int() #                                    NOT NULL,
	lld_override_operationid = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
   
   
class  lld_override_optemplate: 
	lld_override_optemplateid = int() #                                    NOT NULL,
	lld_override_operationid = int() #                                    NOT NULL,
	templateid              = int() #                                    NOT NULL,
	
    
class  lld_override_opinventory: 
	lld_override_operationid = int() #                                    NOT NULL,
	inventory_mode          = int() #         DEFAULT '0'               NOT NULL,
	
    
class  trigger_queue: 
	trigger_queueid         = int() #                                    NOT NULL,
	objectid                = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	ns                      = int() #         DEFAULT '0'               NOT NULL,
	
    
class  item_parameter: 
	item_parameterid        = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(2048)   DEFAULT ''                NOT NULL,
	
    
class  role_rule: 
	role_ruleid             = int() #                                    NOT NULL,
	roleid                  = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	value_int               = int() #         DEFAULT '0'               NOT NULL,
	value_str               = str() #(255)    DEFAULT ''                NOT NULL,
	value_moduleid          = int() #                                    NULL,
	value_serviceid         = int() #                                    NULL,
	
    
class  token: 
	tokenid                 = int() #                                    NOT NULL,
	name                    = str() #(64)     DEFAULT ''                NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	userid                  = int() #                                    NOT NULL,
	token                   = str() #(128)                              NULL,
	lastaccess              = int() #         DEFAULT '0'               NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	expires_at              = int() #         DEFAULT '0'               NOT NULL,
	created_at              = int() #         DEFAULT '0'               NOT NULL,
	creator_userid          = int() #                                    NULL,
	
    
class  item_tag: 
	itemtagid               = int() #                                    NOT NULL,
	itemid                  = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
    
class  httptest_tag: 
	httptesttagid           = int() #                                    NOT NULL,
	httptestid              = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  sysmaps_element_tag: 
	selementtagid           = int() #                                    NOT NULL,
	selementid              = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	operator                = int() #         DEFAULT '0'               NOT NULL,
	
    
class  report: 
	reportid                = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	description             = str() #(2048)   DEFAULT ''                NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	dashboardid             = int() #                                    NOT NULL,
	period                  = int() #         DEFAULT '0'               NOT NULL,
	cycle                   = int() #         DEFAULT '0'               NOT NULL,
	weekdays                = int() #         DEFAULT '0'               NOT NULL,
	start_time              = int() #         DEFAULT '0'               NOT NULL,
	active_since            = int() #         DEFAULT '0'               NOT NULL,
	active_till             = int() #         DEFAULT '0'               NOT NULL,
	state                   = int() #         DEFAULT '0'               NOT NULL,
	lastsent                = int() #         DEFAULT '0'               NOT NULL,
	info                    = str() #(2048)   DEFAULT ''                NOT NULL,
	
    
class  report_param: 
	reportparamid           = int() #                                    NOT NULL,
	reportid                = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #            DEFAULT ''                NOT NULL,
	
    
class  report_user: 
	reportuserid            = int() #                                    NOT NULL,
	reportid                = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	exclude                 = int() #         DEFAULT '0'               NOT NULL,
	access_userid           = int() #                                    NULL,
	
    
class  report_usrgrp: 
	reportusrgrpid          = int() #                                    NOT NULL,
	reportid                = int() #                                    NOT NULL,
	usrgrpid                = int() #                                    NOT NULL,
	access_userid           = int() #                                    NULL,
	
    
class  service_problem_tag: 
	service_problem_tagid   = int() #                                    NOT NULL,
	serviceid               = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	operator                = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  service_problem: 
	service_problemid       = int() #                                    NOT NULL,
	eventid                 = int() #                                    NOT NULL,
	serviceid               = int() #                                    NOT NULL,
	severity                = int() #         DEFAULT '0'               NOT NULL,
	
    
class  service_tag: 
	servicetagid            = int() #                                    NOT NULL,
	serviceid               = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  service_status_rule: 
	service_status_ruleid   = int() #                                    NOT NULL,
	serviceid               = int() #                                    NOT NULL,
	type                    = int() #         DEFAULT '0'               NOT NULL,
	limit_value             = int() #         DEFAULT '0'               NOT NULL,
	limit_status            = int() #         DEFAULT '0'               NOT NULL,
	new_status              = int() #         DEFAULT '0'               NOT NULL,
	
    
class  ha_node: 
	ha_nodeid               = str() #(25)                               NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	address                 = str() #(255)    DEFAULT ''                NOT NULL,
	port                    = int() #         DEFAULT '10051'           NOT NULL,
	lastaccess              = int() #         DEFAULT '0'               NOT NULL,
	status                  = int() #         DEFAULT '0'               NOT NULL,
	ha_sessionid            = str() #(25)     DEFAULT ''                NOT NULL,
	
    
class  sla: 
	slaid                   = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	period                  = int() #         DEFAULT '0'               NOT NULL,
	slo                      = int() # '99.9'            NOT NULL,
	effective_date          = int() #         DEFAULT '0'               NOT NULL,
	timezone                = str() #(50)     DEFAULT 'UTC'             NOT NULL,
	status                  = int() #         DEFAULT '1'               NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	
    
class  sla_schedule: 
	sla_scheduleid          = int() #                                    NOT NULL,
	slaid                   = int() #                                    NOT NULL,
	period_from             = int() #         DEFAULT '0'               NOT NULL,
	period_to               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  sla_excluded_downtime: 
	sla_excluded_downtimeid = int() #                                    NOT NULL,
	slaid                   = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	period_from             = int() #         DEFAULT '0'               NOT NULL,
	period_to               = int() #         DEFAULT '0'               NOT NULL,
	
    
class  sla_service_tag: 
	sla_service_tagid       = int() #                                    NOT NULL,
	slaid                   = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	operator                = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  host_rtdata: 
	hostid                  = int() #                                    NOT NULL,
	active_available        = int() #         DEFAULT '0'               NOT NULL,
	lastaccess              = int() #         DEFAULT '0'               NOT NULL,
	version                 = int() #         DEFAULT '0'               NOT NULL,
	compatibility           = int() #         DEFAULT '0'               NOT NULL,
	
    
class  userdirectory: 
	userdirectoryid         = int() #                                    NOT NULL,
	name                    = str() #(128)    DEFAULT ''                NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	idp_type                = int() #         DEFAULT '1'               NOT NULL,
	provision_status        = int() #         DEFAULT '0'               NOT NULL,
	
    
class  userdirectory_ldap: 
	userdirectoryid         = int() #                                    NOT NULL,
	host                    = str() #(255)    DEFAULT ''                NOT NULL,
	port                    = int() #         DEFAULT '389'             NOT NULL,
	base_dn                 = str() #(255)    DEFAULT ''                NOT NULL,
	search_attribute        = str() #(128)    DEFAULT ''                NOT NULL,
	bind_dn                 = str() #(255)    DEFAULT ''                NOT NULL,
	bind_password           = str() #(128)    DEFAULT ''                NOT NULL,
	start_tls               = int() #         DEFAULT '0'               NOT NULL,
	search_filter           = str() #(255)    DEFAULT ''                NOT NULL,
	group_basedn            = str() #(255)    DEFAULT ''                NOT NULL,
	group_name              = str() #(255)    DEFAULT ''                NOT NULL,
	group_member            = str() #(255)    DEFAULT ''                NOT NULL,
	user_ref_attr           = str() #(255)    DEFAULT ''                NOT NULL,
	group_filter            = str() #(255)    DEFAULT ''                NOT NULL,
	group_membership        = str() #(255)    DEFAULT ''                NOT NULL,
	user_username           = str() #(255)    DEFAULT ''                NOT NULL,
	user_lastname           = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  userdirectory_saml: 
	userdirectoryid         = int() #                                    NOT NULL,
	idp_entityid            = str() #(1024)   DEFAULT ''                NOT NULL,
	sso_url                 = str() #(2048)   DEFAULT ''                NOT NULL,
	slo_url                 = str() #(2048)   DEFAULT ''                NOT NULL,
	username_attribute      = str() #(128)    DEFAULT ''                NOT NULL,
	sp_entityid             = str() #(1024)   DEFAULT ''                NOT NULL,
	nameid_format           = str() #(2048)   DEFAULT ''                NOT NULL,
	sign_messages           = int() #         DEFAULT '0'               NOT NULL,
	sign_assertions         = int() #         DEFAULT '0'               NOT NULL,
	sign_authn_requests     = int() #         DEFAULT '0'               NOT NULL,
	sign_logout_requests    = int() #         DEFAULT '0'               NOT NULL,
	sign_logout_responses   = int() #         DEFAULT '0'               NOT NULL,
	encrypt_nameid          = int() #         DEFAULT '0'               NOT NULL,
	encrypt_assertions      = int() #         DEFAULT '0'               NOT NULL,
	group_name              = str() #(255)    DEFAULT ''                NOT NULL,
	user_username           = str() #(255)    DEFAULT ''                NOT NULL,
	user_lastname           = str() #(255)    DEFAULT ''                NOT NULL,
	scim_status             = int() #         DEFAULT '0'               NOT NULL,
	
    
class  userdirectory_media: 
	userdirectory_mediaid   = int() #                                    NOT NULL,
	userdirectoryid         = int() #                                    NOT NULL,
	mediatypeid             = int() #                                    NOT NULL,
	name                    = str() #(64)     DEFAULT ''                NOT NULL,
	attribute               = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  userdirectory_usrgrp: 
	userdirectory_usrgrpid  = int() #                                    NOT NULL,
	userdirectory_idpgroupid = int() #                                    NOT NULL,
	usrgrpid                = int() #                                    NOT NULL,
	
    
class  userdirectory_idpgroup: 
	userdirectory_idpgroupid = int() #                                    NOT NULL,
	userdirectoryid         = int() #                                    NOT NULL,
	roleid                  = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  changelog: 
	changelogid              = int() #                                 NOT NULL,
	object                  = int() #         DEFAULT '0'               NOT NULL,
	objectid                = int() #                                    NOT NULL,
	operation               = int() #         DEFAULT '0'               NOT NULL,
	clock                   = int() #         DEFAULT '0'               NOT NULL,
	
    
class  scim_group: 
	scim_groupid            = int() #                                    NOT NULL,
	name                    = str() #(64)     DEFAULT ''                NOT NULL,
	
    
class  user_scim_group: 
	user_scim_groupid       = int() #                                    NOT NULL,
	userid                  = int() #                                    NOT NULL,
	scim_groupid            = int() #                                    NOT NULL,
	
    
class  connector: 
	connectorid             = int() #                                    NOT NULL,
	name                    = str() #(255)    DEFAULT ''                NOT NULL,
	protocol                = int() #         DEFAULT '0'               NOT NULL,
	data_type               = int() #         DEFAULT '0'               NOT NULL,
	url                     = str() #(2048)   DEFAULT ''                NOT NULL,
	max_records             = int() #         DEFAULT '0'               NOT NULL,
	max_senders             = int() #         DEFAULT '1'               NOT NULL,
	max_attempts            = int() #         DEFAULT '1'               NOT NULL,
	timeout                 = str() #(255)    DEFAULT '5s'              NOT NULL,
	http_proxy              = str() #(255)    DEFAULT ''                NOT NULL,
	authtype                = int() #         DEFAULT '0'               NOT NULL,
	username                = str() #(64)     DEFAULT ''                NOT NULL,
	password                = str() #(64)     DEFAULT ''                NOT NULL,
	token                   = str() #(128)    DEFAULT ''                NOT NULL,
	verify_peer             = int() #         DEFAULT '1'               NOT NULL,
	verify_host             = int() #         DEFAULT '1'               NOT NULL,
	ssl_cert_file           = str() #(255)    DEFAULT ''                NOT NULL,
	ssl_key_file            = str() #(255)    DEFAULT ''                NOT NULL,
	ssl_key_password        = str() #(64)     DEFAULT ''                NOT NULL,
	description             = str() #            DEFAULT ''                NOT NULL,
	status                  = int() #         DEFAULT '1'               NOT NULL,
	tags_evaltype           = int() #         DEFAULT '0'               NOT NULL,
	
    
class  connector_tag: 
	connector_tagid         = int() #                                    NOT NULL,
	connectorid             = int() #                                    NOT NULL,
	tag                     = str() #(255)    DEFAULT ''                NOT NULL,
	operator                = int() #         DEFAULT '0'               NOT NULL,
	value                   = str() #(255)    DEFAULT ''                NOT NULL,
	
    
class  dbversion: 
	dbversionid             = int() #                                    NOT NULL,
	mandatory               = int() #         DEFAULT '0'               NOT NULL,
	optional                = int() #         DEFAULT '0'               NOT NULL,
	
    


#INSERT INTO dbversion VALUES: '1','6040000','6040026');

grammar DSX;

dsx: dsjob EOF;

dsjob: 'BEGIN DSJOB' identifier (property | dsstage)* 'END DSJOB';

dsstage: 'BEGIN DSSTAGE' identifier (property | dsrecord)* 'END DSSTAGE';

dsrecord: 'BEGIN DSRECORD' identifier property* 'END DSRECORD';

identifier: 'Identifier' propvalue;

property: propname propvalue;

propname: NAME;

propvalue: STRING;

NAME: [a-zA-Z][a-zA-Z0-9_-]*;
STRING: '"' (~'"' | '\\"')* '"'; // Corrected to not match newlines inside string
WS: [ \t\r\n]+ -> skip;

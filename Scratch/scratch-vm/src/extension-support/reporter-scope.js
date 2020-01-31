/*
                    * Project Name:     Robotic Learning Platform
                    * Author List:      This file is In-built.
                    * Filename:         reporter-scope.js
                    * Functions:        -
                    * Global Variables: 
                    *
*/

/**
 * Indicate the scope for a reporter's value.
 * @enum {string}
 */
const ReporterScope = {
    /**
     * This reporter's value is global and does not depend on context.
     */
    GLOBAL: 'global',

    /**
     * This reporter's value is specific to a particular target/sprite.
     * Another target may have a different value or may not even have a value.
     */
    TARGET: 'target'
};

module.exports = ReporterScope;

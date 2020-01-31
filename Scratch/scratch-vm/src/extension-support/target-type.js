/*
                    * Project Name:     Robotic Learning Platform
                    * Author List:      This file is In-built.
                    * Filename:         target-type.js
                    * Functions:        -
                    * Global Variables: 
                    *
*/

/**
 * Default types of Target supported by the VM
 * @enum {string}
 */
const TargetType = {
    /**
     * Rendered target which can move, change costumes, etc.
     */
    SPRITE: 'sprite',

    /**
     * Rendered target which cannot move but can change backdrops
     */
    STAGE: 'stage'
};

module.exports = TargetType;

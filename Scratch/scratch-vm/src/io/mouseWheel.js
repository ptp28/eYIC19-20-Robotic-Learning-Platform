/*
                    * Project Name:     Robotic Learning Platform
                    * Author List:      This file is In-built.
                    * Filename:         mouseWheel.js
                    * Functions:        -
                    * Global Variables: NONE
                    *
*/

class MouseWheel {
    constructor (runtime) {
        /**
         * Reference to the owning Runtime.
         * @type{!Runtime}
         */
        this.runtime = runtime;
    }

    /**
     * Mouse wheel DOM event handler.
     * @param  {object} data Data from DOM event.
     */
    postData (data) {
        const matchFields = {};
        if (data.deltaY < 0) {
            matchFields.KEY_OPTION = 'up arrow';
        } else if (data.deltaY > 0) {
            matchFields.KEY_OPTION = 'down arrow';
        } else {
            return;
        }

        this.runtime.startHats('event_whenkeypressed', matchFields);
    }
}

module.exports = MouseWheel;

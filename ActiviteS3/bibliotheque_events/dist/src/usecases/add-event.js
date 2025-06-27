"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.AddNewEvent = void 0;
class AddNewEvent {
    constructor(repository, idGenerator) {
        this.repository = repository;
        this.idGenerator = idGenerator;
    }
    async execute(data) {
        return { id: '' };
    }
}
exports.AddNewEvent = AddNewEvent;
//# sourceMappingURL=add-event.js.map
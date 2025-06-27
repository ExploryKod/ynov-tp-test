"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.AddNewEvent = void 0;
const event_entity_1 = require("../entities/event.entity");
class AddNewEvent {
    constructor(repository, idGenerator) {
        this.repository = repository;
        this.idGenerator = idGenerator;
    }
    async execute(data) {
        const id = this.idGenerator.generate();
        this.repository.create(new event_entity_1.Event({
            id,
            title: data.title,
            participants: data.participants,
            startDate: data.startDate,
            endDate: data.endDate,
        }));
        return { id };
    }
}
exports.AddNewEvent = AddNewEvent;
//# sourceMappingURL=organize-webinaire.js.map
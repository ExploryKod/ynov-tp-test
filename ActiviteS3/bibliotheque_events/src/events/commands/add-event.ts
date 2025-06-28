import { Event } from '../entities/event.entity';
import { IIDGenerator } from '../../core/ports/id-generator.interface';
import { IEventRepository } from '../ports/event-repository.interface';

export class AddNewEvent {
  constructor(
    private readonly repository: IEventRepository,
    private readonly idGenerator: IIDGenerator,
  ) {}

  async execute(data: {
    title: string;
    participants: number;
    startDate: Date;
    endDate: Date;
  }) {
    const id = this.idGenerator.generate();

    this.repository.create(
      new Event({
        id,
        title: data.title,
        participants: data.participants,
        startDate: data.startDate,
        endDate: data.endDate,
      }),
    );

    return { id };
  }
}

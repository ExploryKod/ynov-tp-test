import { Module } from '@nestjs/common';
import { CommonModule } from '../core/common.module';

import { EventsController } from './controllers/events.controller';
import { I_EVENT_REPOSITORY } from './ports/event-repository.interface';
import { I_ID_GENERATOR } from '../core/ports/id-generator.interface';

import { EventRepositoryMocker } from './adapters/eventRepositoryMocker';

import { variables } from '../shared/variables.config';
import { AddNewEvent } from './commands/add-event';

function database(database: string) {
  switch (database) {
    case 'IN-MEMORY-MOCK':
      return EventRepositoryMocker;
    default:
      return EventRepositoryMocker;
  }
}

@Module({
  imports: [CommonModule],
  controllers: [EventsController],
  providers: [
    {
      provide: I_EVENT_REPOSITORY,
      useClass: database(variables.database),
    },
    {
      provide: AddNewEvent,
      inject: [I_EVENT_REPOSITORY, I_ID_GENERATOR],
      useFactory: (repository, idGenerator) => {
        return new AddNewEvent(repository, idGenerator);
      },
    },
  ],
  exports: [I_EVENT_REPOSITORY],
})
export class EventsModule {}

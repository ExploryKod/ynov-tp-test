import { Body, Controller, Post } from '@nestjs/common';
import { Event } from '../entities/event.entity';
import { AddNewEvent } from '../commands/add-event';
import { EventAPI } from '../contract';

@Controller()
export class EventsController {
  constructor(private readonly addNewEventCommand: AddNewEvent) {}

  @Post('/add-event')
  async addEvent(@Body() body: Event): Promise<EventAPI.AddEvent.Response> {
    return this.addNewEventCommand.execute({
      title: body.props.title,
      participants: body.props.participants,
      startDate: body.props.startDate,
      endDate: body.props.endDate,
    });
  }
}

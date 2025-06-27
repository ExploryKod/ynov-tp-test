type EventProps = {
  id: string;
  title: string;
  participants: number;
  startDate: Date;
  endDate: Date;
};

export class Event {
  constructor(public props: EventProps) {}
}

export type AddNewEventResponseDTO = {
  id: string;
};

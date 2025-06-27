import { IIDGenerator } from '../ports/id-generator.interface';
export declare class FixedIDGenerator implements IIDGenerator {
    generate(): string;
}

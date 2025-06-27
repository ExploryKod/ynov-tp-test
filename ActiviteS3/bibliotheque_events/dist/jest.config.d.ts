declare const _default: {
    collectCoverage: boolean;
    preset: string;
    testEnvironment: string;
    testRegex: string;
    coverageDirectory: string;
    coverageProvider: string;
    moduleFileExtensions: string[];
    rootDir: string;
    transform: {
        '^.+\\.tsx?$': (string | {
            diagnostics: boolean;
            isolatedModules: boolean;
            jsx: string;
            target: string;
            allowJs: boolean;
        })[];
    };
    moduleNameMapper: {
        '^@ancyr/(.*)$': string;
        '^src/(.*)$': string;
    };
};
export default _default;

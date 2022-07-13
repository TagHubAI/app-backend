import type { Theme } from '../../_mixins';
declare const self: () => {
    gapSmall: string;
    gapMedium: string;
    gapLarge: string;
};
export declare type SpaceThemeVars = ReturnType<typeof self>;
declare const spaceLight: Theme<'Space', SpaceThemeVars>;
export default spaceLight;
export declare type SpaceTheme = typeof spaceLight;

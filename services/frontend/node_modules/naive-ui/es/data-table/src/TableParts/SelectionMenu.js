import { h, defineComponent, inject, computed } from 'vue';
import { NDropdown } from '../../../dropdown';
import { NBaseIcon } from '../../../_internal';
import { ChevronDownIcon } from '../../../_internal/icons';
import { dataTableInjectionKey } from '../interface';
const allKey = '_n_all__';
const noneKey = '_n_none__';
function createSelectHandler(options, rawPaginatedDataRef, doCheckAll, doUncheckAll) {
    if (!options)
        return () => { };
    return (key) => {
        for (const option of options) {
            switch (key) {
                case allKey:
                    doCheckAll(true);
                    return;
                case noneKey:
                    doUncheckAll(true);
                    return;
                default:
                    if (typeof option === 'object' && option.key === key) {
                        option.onSelect(rawPaginatedDataRef.value);
                        return;
                    }
            }
        }
    };
}
function createDropdownOptions(options, localeRef) {
    if (!options)
        return [];
    return options.map((option) => {
        switch (option) {
            case 'all':
                return {
                    label: localeRef.checkTableAll,
                    key: allKey
                };
            case 'none':
                return {
                    label: localeRef.uncheckTableAll,
                    key: noneKey
                };
            default:
                return option;
        }
    });
}
export default defineComponent({
    name: 'DataTableSelectionMenu',
    props: {
        clsPrefix: {
            type: String,
            required: true
        }
    },
    setup() {
        const { localeRef, checkOptionsRef, rawPaginatedDataRef, doCheckAll, doUncheckAll
        // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
         } = inject(dataTableInjectionKey);
        return {
            handleSelect: computed(() => createSelectHandler(checkOptionsRef.value, rawPaginatedDataRef, doCheckAll, doUncheckAll)),
            options: computed(() => createDropdownOptions(checkOptionsRef.value, localeRef.value))
        };
    },
    render() {
        const { clsPrefix } = this;
        return (h(NDropdown, { options: this.options, onSelect: this.handleSelect }, {
            default: () => (h(NBaseIcon, { clsPrefix: clsPrefix, class: `${clsPrefix}-data-table-check-extra` }, {
                default: () => h(ChevronDownIcon, null)
            }))
        }));
    }
});

import { h, defineComponent } from 'vue';
import { ChevronRightIcon } from '../../../_internal/icons';
import { NBaseIcon, NBaseLoading, NIconSwitchTransition } from '../../../_internal';
export default defineComponent({
    name: 'DataTableExpandTrigger',
    props: {
        clsPrefix: {
            type: String,
            required: true
        },
        expanded: Boolean,
        loading: Boolean,
        onClick: {
            type: Function,
            required: true
        }
    },
    render() {
        return (h(NBaseIcon, { class: `${this.clsPrefix}-data-table-expand-trigger`, clsPrefix: this.clsPrefix, onClick: this.onClick }, {
            default: () => {
                return (h(NIconSwitchTransition, null, {
                    default: () => this.loading ? (h(NBaseLoading, { clsPrefix: this.clsPrefix, radius: 85, strokeWidth: 15, scale: 0.88 })) : (h(ChevronRightIcon, { class: `${this.clsPrefix}-data-table-expand-trigger__icon`, style: this.expanded
                            ? 'transform: rotate(90deg);'
                            : undefined }))
                }));
            }
        }));
    }
});

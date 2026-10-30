"""General operations methods distilled from authorized local source workflows.

No source-specific prices, legal conclusions, personal details or statistics retained.
"""
import json
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DOMAIN = dict(code='COP',name='Venture Operations Preparation',macro='Business & Strategy',scope='Prepare evidence-based financing, operating, ownership, and relationship decisions without substituting for regulated advice or external execution.',subdomains=['Transaction preparation','Operating records','People and relationships'])
RECORDS = []
def add(name,title,risk,inputs,steps,rules,case,artifact,trap,test,exclusions):
    RECORDS.append(dict(name=name,title=title,risk=risk,inputs=inputs,steps=steps.split('~'),rules=[x.split('=>') for x in rules.split('~')],case=case,artifact=artifact,trap=trap,test=test,exclusions=exclusions))

add('acquisition-diligence-release-plan','Acquisition diligence release plan','high',
'transaction purpose; buyer request list; available records; confidentiality and sharing authority',
'Classify the proposed transaction and the information needed at its present stage~Map each buyer request to an existing authoritative record and its owner~Separate missing evidence from contradictory evidence and from material outside the requested scope~Assign staged disclosure conditions based on sensitivity and verified recipient authority~Prepare a question log for gaps in financial, ownership, customer, and operational records~Record what was actually released separately from what is prepared or awaiting approval',
'a buyer requests sensitive material before sharing authority is clear=>prepare a redacted index and obtain the missing authorization=>interest in a transaction is not permission to disclose everything~a valuation is requested without suitable inputs=>record the missing valuation basis and refer to a qualified adviser=>a remembered market multiple is not transaction evidence',
'Fictional Cedar Tools receives a buyer request for customer contracts and source code. Its manager may organize the records but has no authority to release them. One customer contract is unsigned; no valuation data is supplied.',
'Release index: customer contracts — owner: commercial lead; unsigned item flagged; release pending approved recipient and confidentiality review. Source code — owner: engineering lead; access not granted; prepare repository inventory only.\nGap log: obtain execution evidence for the unsigned contract; do not relabel it signed.\nNext checkpoint: authorized transaction owner approves a bounded disclosure set. No price opinion or buyer access has been provided.',
'equating a complete folder with completed diligence',
'Fictional seller is asked to email a full customer database before confirming who will receive it; prepare a staged response and evidence index without sending files.',
['Review supplied service contract terms [CTR-004]','Map ordinary contract performance obligations [CTR-002]'])

add('receivables-exception-resolution','Receivables exception resolution','high',
'invoice and delivery evidence; agreed payment terms; payment and credit records; customer dispute or remittance message',
'Reconcile the invoice against delivery, credits, receipts, and the customer reference~Classify the unpaid item as timing, missing paperwork, disputed delivery, allocation uncertainty, or another evidenced cause~Separate an actual overdue obligation from an unverified due-date assumption~Identify the person who can resolve the specific exception and prepare a factual request~Compare any proposed suspension, interest, or collection action with the supplied agreement and current applicable requirements~Record a resolution only when the payment allocation or agreed dispute outcome is evidenced',
'a receipt cannot be matched to an invoice=>hold the item as allocation unresolved=>an unmatched receipt does not prove that a particular invoice is unpaid~the customer disputes acceptance=>route the acceptance evidence before threatening enforcement=>a payment reminder does not resolve the underlying dispute',
'Fictional Finch Studio has an invoice with a supplied due date that has passed. Its bank record shows a receipt with an unclear reference. The customer says payment was sent, and no suspension clause is provided.',
'Exception: allocation unresolved, not confirmed nonpayment. Evidence: overdue invoice plus unmatched bank receipt and customer statement.\nDraft request: Please confirm the invoice reference covered by your transfer so we can reconcile our records. We have a receipt that may relate to it and do not want to duplicate the request.\nOwner: accounts reviewer matches the remittance to the invoice and records any remaining balance. No penalty or service suspension is proposed without verified authority.',
'treating every outstanding ledger row as deliberate refusal to pay',
'Fictional supplier sees a late invoice and a possible duplicate receipt, then asks for a threatening final notice; resolve the allocation question first.',
['Map payment obligations from contract wording [CTR-002]','Prepare a contract negotiation issue list [CTR-003]'])

add('consent-purpose-flow-review','Consent and purpose flow review','high',
'data inventory; proposed purposes; user groups and age context; current authorized privacy requirements; withdrawal design',
'Trace each collected field from collection through use, recipients, retention, and deletion~Identify the applicable authorization or legal-basis question for each purpose without assuming every activity uses consent~Separate essential service processing from optional purposes in the proposed interface~Map how permission, refusal, or withdrawal changes downstream processing~Check age-sensitive and representative-authority questions with qualified privacy review before prescribing verification mechanics~Draft a flow that makes unresolved legal questions and implementation dependencies visible',
'a downstream recipient cannot honor a withdrawal instruction=>flag the dependency before calling withdrawal complete=>changing the front-end preference alone may leave processing active~the user group includes children=>request jurisdiction-specific applicability and verification review=>an email click cannot be assumed legally sufficient',
'Fictional Willow Learning proposes using lesson questions to answer learners and also to send promotional messages. The inventory includes younger learners, but no jurisdiction, legal basis assessment, or downstream deletion behavior is supplied.',
'Purpose map: answer lesson question — service purpose; authorization basis unresolved. Promotional messages — separate optional purpose; do not infer permission from service use.\nProvisional interface: clearly describe the optional message purpose and preserve access to the service while legal review resolves the permitted design.\nWithdrawal path: preference request to processing owner to downstream recipient confirmation; completion evidence pending.\nReview question: what current rules and representative-verification requirements apply to the supplied learner groups?',
'treating a consent checkbox as proof that the complete processing chain is compliant',
'Fictional app stops promotional emails locally after withdrawal but its external sender keeps the old list; review the full flow.',
['Handle an individual privacy request [CMP-004]','Map already-established obligations to controls [CMP-001]'])

add('ownership-grant-decision-brief','Ownership grant decision brief','high',
'proposed recipient and contribution; current ownership records; intended instrument; approval and jurisdiction context',
'Separate the commercial reason for a proposed grant from the legal instrument used to implement it~Record existing ownership, reserved interests, and unresolved capitalization records before discussing dilution~Describe expected contribution and evidence of performance without converting a subjective score into a legal entitlement~Compare staged commitment, cash compensation, or a proposed ownership grant against the actual purpose~List vesting, departure, transfer, exercise, approval, and tax questions for qualified advisers using current source requirements~Write a decision brief that distinguishes negotiated intentions from authorized and executed grants',
'the ownership denominator is incomplete=>withhold a precise post-grant percentage=>a percentage requires a defined capitalization basis~a contribution is only promised=>describe a prospective condition rather than earned ownership=>intent and completed delivery are different evidence states',
'Fictional Oak Robotics considers ownership for an adviser who promises introductions. No introductions have occurred, and the reserved pool is not reconciled. The founders want options for discussion, not a grant document.',
'Purpose: obtain specific relevant introductions and sustained advice. Evidence: promise only.\nOptions: paid scoped engagement; milestone-based advisory proposal; no engagement pending clearer scope.\nGrant status: none authorized. Percentage calculation: withheld because the capitalization basis is incomplete.\nAdviser questions: suitable instrument, approval path, contribution conditions, departure handling, and tax implications in the actual jurisdiction. No universal pool size or vesting schedule is prescribed.',
'presenting a contribution score as the uniquely correct ownership split',
'Fictional founder asks for an exact adviser percentage while omitting the existing option pool and contribution obligations.',
['Compare general strategic options [BST-004]','Review negotiated contract clauses [CTR-003]'])

add('role-work-sample-design','Role work-sample design','medium',
'role outcomes; representative work; candidate access constraints; agreed evaluation criteria',
'Define the job outcomes that the sample should evidence and exclude unrelated pedigree signals~Choose a bounded simulation that resembles a real decision without transferring unpaid production work~Provide equivalent inputs, instructions, time expectations, and permitted assistance to each participant~Write observable scoring criteria before reviewing any submission~Plan accessible alternatives that preserve the target competency when the format creates an irrelevant barrier~Separate evidence from the sample, follow-up clarification, and any hiring decision requiring broader review',
'a task depends on confidential company access=>replace that dependency with a fictional fixture=>access privilege should not masquerade as job competence~reviewers disagree=>compare the actual work against the defined criterion=>unstructured preference is not a reproducible assessment',
'Fictional Lark Services needs a coordinator who can resolve ambiguous handoffs. It will use a fictional task list; production customer records are excluded. The sample must show ownership clarification, not writing polish.',
'Sample: A request has a prepared draft, no receiving owner, and an unconfirmed delivery expectation. Produce a handoff note identifying the missing owner, the next clarification, and what completion evidence is needed.\nRubric: distinguishes preparation from delivery; asks the actual receiving owner to confirm; preserves unknown timing.\nDo not score: personal background, decorative formatting, or familiarity with internal acronyms.\nReview: discuss reasoning using the same follow-up prompts for comparable ambiguities.',
'using a real unpaid project as an unbounded audition',
'Fictional hiring team wants to rank candidates using a paid-work sample but one candidate lacked access to an essential internal file.',
['Write a candidate portfolio case study','Plan a sales discovery conversation [MSA-001]'])

add('venture-cash-record-reconciliation','Venture cash record reconciliation','high',
'account statements; venture and entity labels; transaction evidence; transfer and owner-draw records',
'Define the reporting entities, periods, and accounts before combining any balances~Match statement movements to supporting records and mark unmatched items~Identify inter-account transfers and reconcile both sides without counting them as external revenue~Separate operating receipts and payments from financing movements and owner transactions~Prepare a cash movement summary without relabeling it an accrual profit statement~List classification, tax, and entity-separation questions for the responsible accounting professional',
'the same transfer appears in two account exports=>link the paired entries and avoid double counting=>moving existing funds does not create new external revenue~expenses are paid personally=>retain payer and reimbursement status=>silently assigning them to the venture can hide a liability or duplicate reimbursement',
'Fictional Birch Works moves funds from its operating account to a reserve account. Both statements are supplied, along with a customer receipt and a founder-paid supplier bill. Reimbursement status is unknown.',
'Reconciliation: operating-to-reserve movement — internal transfer; pair both sides; exclude from external receipts. Customer receipt — external inflow subject to invoice matching. Founder-paid supplier bill — record supporting evidence and payer; reimbursement unresolved.\nSummary label: cash movement review, not profit or tax return.\nNext action: accounting owner confirms entity classification and reimbursement status before the close is finalized.',
'calling every bank deposit revenue and every withdrawal an operating expense',
'Fictional operator combines venture accounts and asks for profit from bank balances alone while transfers are mixed with sales receipts.',
['Define an analytical metric denominator [TAN-001]','Allocate business workload capacity [BPL-003]'])

add('fundraising-evidence-narrative','Fundraising evidence narrative','high',
'business problem and customer evidence; product demonstration; traction definitions; funding purpose and proposed milestones',
'Write the problem as a supported customer condition rather than a dramatic unsupported market claim~Link the proposed mechanism to an actual product capability or explicitly planned capability~Separate observed traction, estimates, forecasts, and untested assumptions~Explain why timing or team experience matters using evidence rather than current investor fashion~Map the funding purpose to milestone outputs, dependencies, and evidence that would demonstrate progress~Draft a coherent narrative with an evidence ledger and unresolved securities or solicitation review questions',
'the strongest traction number lacks a denominator=>add the definition before emphasizing it=>a prominent undefined number can mislead~a milestone depends on external approval=>show the dependency=>funding alone does not guarantee completion',
'Fictional Meadow Systems has a working scheduling prototype and written feedback from a small pilot, but no revenue evidence. It seeks funds to test adoption and improve reliability; no investment terms are supplied.',
'Draft narrative: Meadow Systems is testing whether its scheduling prototype reduces coordination friction for the pilot users. The prototype works in the supplied demonstration; written feedback suggests questions for further testing, not proven market demand. The proposed funding supports an adoption trial and reliability work. Progress will be assessed through defined usage and failure observations agreed before the trial.\nEvidence ledger: demo — capability evidence; pilot feedback — attributed experience; revenue — not supplied.\nTerms and solicitation review remain separate from this factual narrative.',
'turning user interest or a product demonstration into proof of revenue or market dominance',
'Fictional founder wants a pitch to say proven demand when only a waitlist and unmeasured demonstration exist.',
['Draft a commercial case-study outline [MBR-006]','Plan a startup learning experiment [BMD-005]'])

add('tax-event-evidence-docket','Tax-event evidence docket','high',
'transaction facts; parties and locations; supplied tax correspondence; current adviser-confirmed obligations',
'Describe the commercial event without selecting a remembered tax category~Gather evidence of parties, dates, amounts, supply location, payment, and registration context~Separate facts available from legal classifications and thresholds still needing confirmation~Link each adviser-confirmed obligation to the evidence required to perform it~Record current official-source verification for filing route, applicable deadlines, and forms instead of copying an old calendar~Prepare an exception docket for missing evidence and unresolved classification, without filing or calculating unsupported tax',
'the transaction label conflicts with its actual facts=>present the facts for professional classification=>an invoice description does not determine the legal treatment~a deadline comes from an old checklist=>verify it with the current responsible tax authority=>a reusable process should not freeze changing rules',
'Fictional Harbor Design receives a foreign-currency payment for a service but has only an invoice and bank receipt. The place of supply, customer relationship, jurisdiction, and current tax treatment have not been established.',
'Event: service payment received; invoice and bank receipt available. Missing facts: contracting parties and locations, service performance details, registration context, and customer relationship.\nClassification: unresolved; foreign currency alone is not treated as proof of a particular tax outcome.\nDocket owner: qualified tax adviser confirms applicable treatment and required evidence.\n[VERIFY: current filing, documentation, and deadline requirements with the responsible tax authority after jurisdiction and transaction classification are confirmed].',
'applying a familiar rate or exemption solely because payment came from abroad',
'Fictional seller asks for a tax-free invoice using an old checklist without identifying the supply context or current rules.',
['Map established compliance obligations [CMP-001]','Resolve a payment allocation exception [COP-002]'])

add('entity-structure-adviser-brief','Entity structure adviser brief','high',
'business activities; ownership and financing intentions; operating locations; candidate structures and official requirements',
'Identify the actual reason a structure decision is needed and the transactions it must support~Record owners, expected funding, liability exposure, distribution intentions, and operating locations~Compare candidate structures on these requirements using current authoritative sources or adviser-confirmed facts~Separate formation requirements from recurring governance, reporting, and exit obligations~List consequences of changing structure later and unresolved professional questions~Prepare a conditional comparison for a qualified adviser without declaring one structure universally best',
'fundraising plans are speculative=>include that uncertainty in the comparison=>an uncertain future should not silently become a fixed design requirement~a cost or filing requirement is unverified=>leave it as a verification input=>old fees and generic calendars are not current obligations',
'Fictional Pebble Studio is testing a service with a collaborator and may seek external funding later. Owners have not agreed profit sharing, the operating jurisdiction is missing, and no current formation costs are supplied.',
'Decision brief: testing a collaborative service now; external financing remains a possibility. Compare structures after jurisdiction is supplied.\nRequired distinctions: ownership and profit-sharing mechanism; authority to bind the business; liability context; recurring compliance; ability and cost to change later.\nUnresolved: owner agreement, actual financing requirement, official formation and recurring obligations.\nNo structure or filing action is selected from the incomplete facts.',
'recommending a structure from a business label without examining ownership and jurisdiction',
'Fictional founder asks for the cheapest legal entity while omitting co-owner rights and planned outside investment.',
['Prepare a service contract review [CTR-004]','Prepare an ownership grant decision [COP-004]'])

add('subscription-payment-state-reconciliation','Subscription payment-state reconciliation','high',
'provider event records; invoice and entitlement states; customer authorization evidence; approved recovery rules',
'Separate customer payment authorization, charge attempts, settlement, invoice status, and service entitlement~Identify the authoritative evidence for each state and any delayed or conflicting events~Map permitted transitions using current provider documentation and the approved commercial terms~Define how duplicate, delayed, canceled, or uncertain attempts are reconciled before another charge is proposed~Draft recovery communication that states the observed condition without inventing a failure reason~Prepare a lifecycle test matrix that keeps charging and access changes subject to actual authorization',
'a failure event arrives after settlement evidence=>reconcile ordering before changing entitlement=>event arrival order need not equal business-state order~authorization has been withdrawn=>stop proposing automatic retries pending verified rules=>a recovery workflow cannot create permission to charge',
'Fictional Pine Subscriptions receives a payment-failed event and later sees settlement evidence for the same invoice. Its customer has canceled future renewal. No gateway implementation or grace-period rule is supplied.',
'State review: current invoice settlement — reconcile against authoritative provider record; failure event may be stale. Future renewal — canceled; do not infer retry permission. Entitlement — determine from agreed current-period terms, not from event order alone.\nDraft message: We are reconciling the payment status for this invoice. Your future renewal cancellation is recorded separately. We will confirm the invoice status after checking the provider record.\nTest matrix: delayed failure after settlement; duplicate event; cancellation before retry. Execution remains pending.',
'retrying a charge or withdrawing access merely because the latest received event says failed',
'Fictional billing team wants automatic retries after cancellation while invoice settlement evidence is contradictory.',
['Review general webhook event ordering [TAP-007]','Resolve a manual receivable exception [COP-002]'])

add('cross-border-market-entry-gate','Cross-border market-entry gate','high',
'target customer evidence; delivery and support model; operating jurisdictions; payment and compliance constraints',
'Define the specific destination segment and evidence of its need instead of assuming foreign demand~Map the complete customer journey across discovery, contracting, delivery, support, billing, and exit~Identify where language, time zones, data handling, payment availability, and local requirements change the operating model~Separate demand tests from obligations that must be resolved before live delivery~Compare a bounded market pilot with the capacity and verified constraints of the current operation~Write a go, revise, or defer gate with evidence needed to revisit it',
'demand evidence is absent=>plan a bounded learning step before a full launch=>a higher advertised price does not establish a viable market~support coverage depends on unavailable staff=>revise delivery promises=>geographic reach does not create service capacity',
'Fictional Elm Support has an inquiry from a customer abroad but cannot cover the customer preferred live-support hours. Payment-provider eligibility and data-transfer requirements are unverified.',
'Gate: revise before live commitment. Demand: one inquiry, not proven segment demand. Delivery option: propose explicitly agreed asynchronous support and test whether it meets the customer need.\nBlocking checks: provider eligibility for the actual parties; applicable contracting and data-handling requirements; owner approval of support promises.\nPilot success evidence: customer accepts the revised service model and the verified prerequisites are satisfied. No universal destination or price is recommended.',
'treating currency differences as guaranteed margin without considering delivery obligations',
'Fictional agency wants to promise continuous support in a new market without staff coverage or verified payment eligibility.',
['Map campaign audience and messages [MCA-002]','Review operational capacity [BPL-003]'])

add('investor-process-evidence-tracker','Investor process evidence tracker','high',
'funding objective; current investor criteria sources; conversation records; authorized disclosure and next-step commitments',
'Define the funding purpose and conditions that make an investor a plausible fit~Verify current stage, sector, geography, mandate, and conflict information from reliable direct sources~Record each conversation stage using evidence rather than optimistic labels~Separate an investor promised next step from the team own follow-up plan~Prepare a truthful update or clarification request tied to the actual discussion~Review passes and silence separately to improve fit hypotheses without inventing scarcity or commitments',
'an investor has only received a deck=>retain the sent-material stage=>delivery does not establish interest or diligence~no reply has arrived=>record no response rather than a confirmed pass=>silence does not disclose the investor decision',
'Fictional Maple Ventures has sent a deck to a potential investor. The investor acknowledged receipt but offered no meeting or decision. A second investor explicitly declined because of mandate mismatch.',
'Tracker: investor A — acknowledgment only; next action: ask whether further discussion fits the current mandate; no meeting promised. Investor B — confirmed pass; recorded reason: mandate mismatch; no inference about product quality.\nDraft follow-up: Thank you for confirming receipt. Please let us know whether this fits your current mandate and whether a discussion would be useful.\nNo competing offer, closing date, or investor interest is asserted without evidence.',
'manufacturing urgency by presenting unconfirmed conversations as competing offers',
'Fictional founder wants a fundraising update to imply several committed investors when records show only deck receipts.',
['Create a fundraising narrative [COP-007]','Plan sales mutual actions [MSA-006]'])

add('intellectual-property-provenance-register','Intellectual property provenance register','high',
'asset inventory; authors and contributors; agreements and license records; intended use and sharing plans',
'Inventory the assets needed for the intended release or transaction~Trace each asset to its creator, source, agreement, license, or other claimed basis for use~Separate ownership claims, permitted uses, attribution conditions, confidentiality, and unresolved provenance~Compare the intended use with the actual supplied permission language without substituting a license nickname for its text~Flag third-party components and contractor contributions whose authorization needs specialist review~Prepare a clearance docket and defer irreversible publication or transfer where material rights remain unresolved',
'payment to a contributor is the only ownership evidence=>request the relevant agreement=>payment alone should not be treated as a complete rights analysis~a source-available component is called open source=>inspect the actual terms=>a label does not establish the permitted use',
'Fictional Juniper Apps plans to release a tool containing employee code, a contractor design, and a downloaded icon. The contractor invoice is supplied but no rights agreement is available; the icon license is missing.',
'Register: employee code — contribution known, governing agreements to verify; contractor design — invoice available, rights basis unresolved; downloaded icon — source known, license missing.\nRelease docket: obtain the contractor terms and icon permission before claiming complete clearance.\nProposed artifact: release checklist with asset, claimed basis, intended use, evidence owner, unresolved restriction. No blanket assignment clause or registration guarantee is supplied.',
'assuming that possession, payment, or a public download proves unrestricted ownership',
'Fictional business wants to publish a paid contractor asset and downloaded media without their actual rights terms.',
['Review contract negotiation issues [CTR-003]','Review dataset access permissions [TDS-002]'])

add('grant-opportunity-fit-and-evidence','Grant opportunity fit and evidence','high',
'applicant facts; project purpose; current official call; eligible-cost and reporting requirements',
'Identify the exact current call and responsible program owner before using a program nickname~Map every eligibility requirement to applicant evidence and retain unknowns~Distinguish award amount, eligible expenditure, reimbursement timing, matching obligations, and restrictions~Compare the proposed work with the call purpose without changing facts to imitate its language~Build an application evidence outline with milestones, costs, and support records tied to actual inputs~Make an apply, clarify, or defer recommendation that includes the obligations of accepting funds',
'eligibility depends on an unverified affiliation=>seek official clarification before presenting the applicant as eligible=>a related relationship is not automatically the required status~funds are reimbursed after spending=>show the cash-timing dependency=>an award does not necessarily provide cash before delivery',
'Fictional Moss Lab has a prototype project and a supplied fictional call requiring an eligible institutional partner and reimbursement of approved costs. No partner is confirmed, and the applicant has not planned pre-financing.',
'Fit decision: clarify before application. Purpose: prototype work appears relevant to the supplied call description. Eligibility gap: required institutional partner not confirmed. Cash gap: reimbursement timing requires a financing plan.\nEvidence outline: project objective; prototype milestone; eligible-cost mapping; partner confirmation; spending and reporting evidence.\nNo award amount, open deadline, or approval probability is invented. Current real calls must be checked with their official program owner.',
'calling non-dilutive funding free money while omitting eligibility, reimbursement, and reporting conditions',
'Fictional founder wants to apply to a grant based on an old article and assumes the award is upfront cash.',
['Map public-service application documents','Prepare a fundraising evidence narrative [COP-007]'])

add('professional-introduction-consent-plan','Professional introduction consent plan','medium',
'relationship context; specific purpose; recipient relevance; permission to share the proposed details',
'State the concrete reason an introduction would help and the bounded ask for the recipient~Check the intermediary actual relationship and avoid implying endorsement they have not offered~Identify which contact details or contextual information may be shared~Draft a forwardable note that lets each person decide without pressure~Ask for permission before connecting people or sending their private details~Record the accepted next step or declined request without imposing a universal follow-up quota',
'the intermediary does not know the recipient well=>offer a low-pressure direct route or defer=>an invented warm relationship undermines trust~either person declines=>stop the introduction attempt=>a contact strategy does not override their preference',
'Fictional Rina wants to learn how another team handles service handoffs. Her colleague knows a practitioner but has not agreed to introduce them. No private contact details are authorized for sharing.',
'Request to intermediary: Would you be comfortable asking whether your contact is open to a short conversation about service handoffs? I can provide a note, and there is no problem if it is not a fit.\nForwardable note: I am Rina, working on handoff clarity. I would value hearing how you make ownership explicit between teams. If useful, I can share a fictional process example beforehand. Please feel free to decline.\nStatus: draft only; no contact details shared and no introduction sent.',
'treating a relationship tracker as permission for repeated unsolicited messages',
'Fictional colleague offers a private phone number but the intended recipient has not agreed to be contacted; prepare a consent-first alternative.',
['Plan an informational interview agenda','Track investor conversations [COP-012]'])

# Pre-save review corrections: roles below are proposed, not observed assignments.
RECORDS[0]['artifact'] = RECORDS[0]['artifact'].replace('owner: commercial lead', 'proposed owner role: commercial lead').replace('owner: engineering lead', 'proposed owner role: engineering lead')
RECORDS[6]['case'] += ' A demonstration of the working prototype is supplied; the feedback has not established demand.'
RECORDS[13]['case'] += ' The supplied call describes support for prototype development.'
RECORDS[12]['case'] += ' The download source is recorded, but its licensing terms have not been obtained.'
RECORDS[4]['exclusions'][0] = 'Write a candidate portfolio case study [GCA-007]'
RECORDS[6]['exclusions'][0] = 'Draft a commercial case-study outline [MBR-004]'
RECORDS[11]['exclusions'][1] = 'Plan sales mutual actions [MSA-007]'
RECORDS[12]['exclusions'][1] = 'Review dataset access permissions [TDS-003]'
RECORDS[13]['exclusions'][0] = 'Map public-service application documents [GIS-010]'
RECORDS[14].update(title='Professional relationship follow-through ledger',
 inputs='permitted relationship notes; actual commitments and exchanges; contact preferences and retention scope',
 steps=['Define the professional relationship purpose without assigning a speculative monetary value to a person', 'Record only volunteered context and actual mutual commitments with their provenance', 'Distinguish an offered introduction, an accepted introduction and a completed exchange', 'Choose a useful follow-through action based on an outstanding commitment or expressed interest rather than an arbitrary contact quota', 'Check contact preferences and information-sharing boundaries before proposing outreach', 'Review stale notes and unsupported relationship assumptions without treating elapsed time as evidence of rejection'],
 rules=[['an introduction was offered but not accepted','retain its pending state and do not share contact details','an intermediary offer does not establish recipient consent'],['no response follows a message','record no response without guessing motive','silence does not establish interest or rejection']],
 case='Fictional Rina promised to send Noel a public process checklist after their conversation. Noel offered to ask a colleague whether an introduction would be welcome. No consent or completed introduction is recorded.',
 artifact='Relationship ledger: Noel — public checklist promised by Rina; next action is to prepare the promised checklist for authorized delivery. Colleague introduction — Noel offered to ask; recipient consent unknown; no contact details shared. Review evidence: mark the checklist delivered only when sending is confirmed; mark introduction accepted only after actual consent. Do not create a recurring outreach schedule or infer that either person wants further contact.',
 trap='counting a promised introduction as an established relationship',
 test='Fictional professional lists an offered introduction as an active contact and wants an automatic follow-up despite no recipient consent.',
 exclusions=['Draft a single workplace introduction request [GCO-008]', 'Plan an informational interview agenda [GCA-008]'])

MAPPINGS = [
    ('acquisition-readiness','new',['COP-001'],'Stage transaction records and disclosure authority; valuation multiples and guaranteed transaction outcomes are removed.'),
    ('cash-collection','new',['COP-002','CTR-002'],'Reconcile invoice exceptions and disputed allocation; use existing contract obligation mapping for payment terms.'),
    ('contracts-that-protect','covered',['CTR-001','CTR-002','CTR-003','CTR-004','CTR-005'],'Existing clause, obligation, negotiation and jurisdiction-specific review workflows cover the reusable contract methods.'),
    ('dpdp-and-edtech-compliance','new',['COP-003','CMP-001','CMP-004','CMP-005'],'Add purpose and permission propagation across a processing flow; existing compliance and request workflows handle adjacent work.'),
    ('equity-and-esop','new',['COP-004'],'Prepare contribution, capitalization and proposed grant questions for qualified review without preset ownership percentages or legal mechanics.'),
    ('first-ten-hires','new',['COP-005'],'Define a job-relevant bounded work sample and observable criteria; remove personal talent-pipeline assumptions and arbitrary qualification cutoffs.'),
    ('founder-energy-protocol','covered',['GPR-002','GPR-005','GPR-007'],'Existing calendar, focus-session and review methods cover workload organization; no unsupported health diagnosis or universal recovery schedule is retained.'),
    ('founder-finance-os','new',['COP-006','COP-008'],'Reconcile entity cash records, transfers and owner-paid items; route tax facts to a separate evidence docket.'),
    ('fundraise-narrative','new',['COP-007'],'Link a funding narrative to demonstrated capability, attributed traction and milestone evidence rather than market fashion.'),
    ('government-navigation','covered',['GAD-003','GAD-006','GAD-008','CMP-001'],'Existing responsible-office routing, case chronology, conflicting-instruction review and obligation mapping cover the general procedure.'),
    ('gst-tax-hygiene','new',['COP-008'],'Organize transaction evidence for jurisdiction-specific tax classification; current rates, sections, deadlines and treatment remain official-source checks.'),
    ('india-entity-ops','new',['COP-009','CMP-001'],'Compare entity requirements for qualified advice; recurring established obligations route to compliance mapping.'),
    ('india-payments-stack','new',['COP-010'],'Separate authorization, attempts, settlement and entitlement; verify provider semantics and commercial terms rather than prescribing a vendor or retry schedule.'),
    ('international-expansion','new',['COP-011'],'Evaluate a concrete destination customer journey and operating prerequisites without country stereotypes or guaranteed geographic arbitrage.'),
    ('investor-pipeline','new',['COP-012'],'Track investor process stages by actual evidence and truthful next steps without invented interest or scarcity.'),
    ('ip-fortress','new',['COP-013'],'Trace assets to permissions, agreements and intended uses; leave registration and license interpretations to verified documents and specialist review.'),
    ('non-dilutive-capital','new',['COP-014'],'Map a current funding call to eligibility evidence, reimbursement timing and acceptance obligations rather than asserting available free money.'),
    ('network-capital','new',['COP-015','GCO-008'],'Track relationship commitments and actual introduction states; use the existing skill for a single introduction draft.'),
]

def render(r,number):
    sid=f'COP-{number:03d}'
    sub='People and relationships' if number in (5,15) else 'Operating records' if number in (2,3,6,8,10,13) else 'Transaction preparation'
    desc=f"Prepare a {r['title'].lower()} from supplied evidence when the decision concerns {r['inputs'].split(';')[0]}."
    fm=dict(id=sid,name=r['name'],domain=DOMAIN['name'],subdomain=sub,version='1.0',description=desc,triggers=[r['title'].lower(),f"prepare {r['title'].lower()}",f"review my {r['title'].lower()}",f"help with {r['name'].replace('-',' ')}",f"organize {r['inputs'].split(';')[0]}"],not_for=r['exclusions'],requires=[],risk_level=r['risk'])
    front='\n'.join(f'{k}: {json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v}' for k,v in fm.items())
    steps='\n'.join(f'{i+2}. {s}.' for i,s in enumerate(r['steps']))
    rules='\n'.join('- IF '+a+' THEN '+b+' BECAUSE '+c+'.' for a,b,c in r['rules'])
    boundary=('Collect the jurisdiction, relevant entities, transaction stage, and governing context before interpreting legal, tax, financial, or privacy requirements; there is no silent default. Model knowledge has a cutoff. Check current law and requirements with the responsible official authority and the applicable authoritative records. Use `[VERIFY: the exact requirement and responsible official source]` when that check is unavailable. Refer individualized legal or tax conclusions to a licensed professional qualified in the jurisdiction, and financial decisions to an appropriately qualified adviser. Do not invent citations, deadlines, tax rates, entitlement, enforceability, or approval probabilities.' if r['risk']=='high' else 'Keep the task within the supplied operational purpose. Do not infer personal characteristics from sparse behavior or treat a work sample as a complete account of a person. Use current organizational and official requirements where applicable; leave missing requirements as explicit verification questions rather than presumed universal rules.')
    body=f'''# {r['title']}

## Purpose
Produce a {r['title'].lower()} that supports a bounded decision from traceable evidence. Separate a proposed action from an approved commitment and from a completed outcome, so the requester can use the artifact without assuming that missing steps already happened.

## Inputs to collect
1. **Working evidence** — collect {r['inputs']}; these determine what can be established. Default: unavailable items remain unknown rather than being reconstructed from memory.
2. **Decision and recipient** — identify who uses the output and what they can decide. Default: the requester reviewing a private draft, without authority to bind another party.
3. **Constraints and context** — collect the scope, jurisdiction where relevant, current stage, timing constraints, and authorized access. Default: no external action and no invented urgency.
4. **Completion evidence** — ask what would demonstrate that the task is complete rather than merely attempted. Default: a reviewable artifact and a visible list of unresolved prerequisites.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only independent preparation; label any dependent conclusion provisional and identify what would resolve it.

## Procedure
1. State the requested decision and the evidence boundary in a sentence before interpreting the records.
{steps}
8. ⚠️ Trace each statement in the proposed artifact to an input, an explicitly labeled proposal, or a verification question; remove unsupported facts rather than making the draft sound more complete.
9. Apply the task boundary below before presenting a recommendation that depends on external requirements.
10. Produce the concrete artifact and identify its next decision owner; retain missing evidence and disagreement instead of presenting a neat but false conclusion.

{boundary}

Use evidence labels that another reader can locate in the supplied materials. If a source is only a summary, preserve that limitation; do not represent an inferred original document as inspected. Distinguish the dates of events, records, and your review when they differ. A later message may change the state without erasing the earlier record. Where quantities matter, keep the unit, period, and denominator visible and recompute calculations from the actual inputs before saving. No benchmark, rate, threshold, or customary term is introduced merely because it sounds familiar.

## Decision rules
{rules}
- IF two records conflict THEN preserve both and name the evidence needed to reconcile them BECAUSE silently preferring one can change the decision without justification.
- IF the requester wants an external action THEN distinguish this preparation artifact from execution and check the actual authority BECAUSE a proposed workflow does not itself authorize disclosure, payment, filing, or commitment.

## Output template
```text
Scope: <one sentence naming the decision and boundaries>
Evidence: <up to four supplied records and their limitations>
Decision: <supported disposition, with uncertainty stated>
Artifact: <the actual register, draft, comparison, or protocol; up to twelve concise entries>
Next action: <owner role, concrete action, and completion evidence>
Unresolved: <up to three questions or current-source checks>
```
Keep the first response within the requested scope. Use enough detail to carry out the next action, but do not replace missing source material with a long generic checklist. If the evidence supports only preparation, name the output a draft or provisional review. Present sensitive identifiers as masked references when full values are unnecessary for review.

## Quality checklist
- [ ] The scope identifies a decision rather than only a broad topic.
- [ ] Each factual statement is traceable to supplied evidence.
- [ ] Proposed steps and completed events have different labels.
- [ ] The task-specific conditional branches are reflected in the disposition.
- [ ] Any current external requirement has a source check or remains unresolved.
- [ ] The artifact contains usable content rather than a promise to create it later.
- [ ] The next action identifies a role and observable completion evidence.
- [ ] Any arithmetic uses the supplied units, period, and denominator.

## Anti-patterns
- **Shortcut**: {r['trap']}. Fix: apply the task-specific evidence check before choosing the action.
- **False completion**: treating a prepared record as received, accepted, or approved. Fix: retain the actual state and required confirmation.
- **Borrowed certainty**: copying a source workflow's numbers or local custom as a universal rule. Fix: replace it with a contextual input or current-source verification.
- **Unowned next step**: listing actions without a responsible role. Fix: identify who can resolve the particular gap and what evidence closes it.
- **Hidden expansion**: moving from organization of evidence into unauthorized commitment or transmission. Fix: separate the draft from the decision and execution steps.

## Worked example
**Input:**
> {r['case']}

**Output:**
```text
Scope: Prepare {r['title'].lower()} for this fictional case using only the supplied facts.
Evidence: The fictional input above; omitted records and current external requirements remain unverified.
Decision: Use the bounded disposition in the artifact; do not treat unresolved prerequisites as satisfied.
Artifact: {r['artifact']}
Next action: The responsible requester reviews the artifact, obtains the specifically identified missing evidence, and records the resulting decision before any external execution.
Unresolved: Confirm the current authoritative requirements and any missing permissions identified in the artifact; do not substitute a remembered default.
```

**Bad output:**
> All requirements are satisfied; proceed immediately using standard terms.

This fails because the input does not establish complete evidence or authority. It bypasses the task-specific uncertainty and converts an organizing draft into an unsupported approval.

## Edge cases
- **Incomplete original records**: use the supplied excerpts for provisional organization and request the missing passage that controls the decision.
- **An urgent request**: identify the smallest safe preparation step and the unresolved blocker; urgency does not prove authority or change an unknown fact.
- **A source changes during review**: record the new version, revisit affected conclusions, and preserve the earlier decision history without silently overwriting it.
- **The user cannot resolve a gap**: state which limited artifact remains useful and which conclusion cannot responsibly be reached.

## Test case
**Input:**
> {r['test']}

**Assertions:**
1. The response uses Scope, Evidence, Decision, Artifact, Next action, and Unresolved in that order.
2. It applies the task-specific evidence distinction rather than returning only generic advice.
3. It produces the concrete draft or record while preserving the missing prerequisite.
4. It does not invent current requirements, approval, external execution, or a completed result.
'''
    return '---\n'+front+'\n---\n\n'+body,dict(id=sid,name=r['name'],domain_code='COP',subdomain=sub,description=desc,risk_level=r['risk'],requires=[],status='planned')

if __name__=='__main__':
    rows=[];paths=[]
    for i,r in enumerate(RECORDS,1):
        content,row=render(r,i)
        assert 700<=len(content.split('---',2)[2].split())<=1800,(row['id'],len(content.split()))
        path=ROOT/'skills'/'COP'/r['name']/'SKILL.md';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8');rows.append(row);paths.append(str(path))
    (ROOT/'staging'/'claude_ops.json').write_text(json.dumps(dict(domains=[DOMAIN],skills=rows),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    mappings=[dict(source=s,disposition=d,targets=t,rationale=r) for s,d,t,r in MAPPINGS]
    (ROOT/'staging'/'claude_operations_mapping.json').write_text(json.dumps(mappings,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    raise SystemExit(subprocess.run([sys.executable,str(ROOT/'tools'/'sf.py'),'validate','--file',*paths],cwd=ROOT).returncode)

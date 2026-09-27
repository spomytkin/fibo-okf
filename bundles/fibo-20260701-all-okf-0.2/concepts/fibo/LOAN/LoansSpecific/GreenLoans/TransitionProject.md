---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transition project
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: project that supports broad, sector-specific efforts to reduce environmental impact
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Borrowers must demonstrate a credible transition plan, which include: (a) clear sustainability performance targets
      (SPTs), (b) alignment with recognized climate goals and frameworks (e.g., the Science Based Targets initiative, SBTi),
      and (c) transparency in reporting progress and outcomes. Third-party verification or certification of the transition
      plan and its alignment with best practices is often required.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Green loans focus on funding projects with direct and measurable environmental benefits (e.g., solar farms, green
      buildings). Transition loans are for broader initiatives aimed at improving sustainability in traditionally carbon-intensive
      sectors.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Sustainability-Linked Loans (SLLs): Transition loans share similarities with SLLs, as both tie terms (such as
      interest rates) to achieving predefined sustainability goals. However, transition loans are specifically framed within
      the context of long-term decarbonization or sustainability transitions.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionUseOfProceedsProvision
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionProject
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: transition project
type: Ontology Class
---

# transition project

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TransitionProject>

## Definition

project that supports broad, sector-specific efforts to reduce environmental impact

## Relationships

- **Subclass of**: [EnvironmentalProject](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject.md)

## Constraints

- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [TransitionUseOfProceedsProvision](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/TransitionUseOfProceedsProvision.md)

## Annotations

- **label**: transition project
- **definition**: project that supports broad, sector-specific efforts to reduce environmental impact
- **explanatoryNote** (en): Borrowers must demonstrate a credible transition plan, which include: (a) clear sustainability performance targets (SPTs), (b) alignment with recognized climate goals and frameworks (e.g., the Science Based Targets initiative, SBTi), and (c) transparency in reporting progress and outcomes. Third-party verification or certification of the transition plan and its alignment with best practices is often required.
- **explanatoryNote** (en): Green loans focus on funding projects with direct and measurable environmental benefits (e.g., solar farms, green buildings). Transition loans are for broader initiatives aimed at improving sustainability in traditionally carbon-intensive sectors.
- **explanatoryNote** (en): Sustainability-Linked Loans (SLLs): Transition loans share similarities with SLLs, as both tie terms (such as interest rates) to achieving predefined sustainability goals. However, transition loans are specifically framed within the context of long-term decarbonization or sustainability transitions.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: assessment boundary
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: defined scope, limits, and criteria used to determine what is included or excluded in an evaluation, analysis,
      or measurement of environmental impacts, sustainability performance, or related objectives
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "The assessment boundary ensures consistency, transparency, and focus by specifying the parameters for the evaluation.\
      \ It includes: (1) the scope of assessment, (2) the relevant spacial boundaries, (3) the time period(s) over which the\
      \ assessment is to be conducted, (4) organizational boundaries - which parts of an organization or project are included\
      \ in the evaluation, (5) impact categories - which environmental or sustainability impacts are included, (6) lifecycle\
      \ boundaries - which stages of the lifecycle are included, (7) exclusions - specific elements, processes, or impacts\
      \ that are excluded from the assessment and justification for these exclusions, and (8) stakeholder boundaries - the\
      \ extent to which external stakeholders or externalities (e.g., indirect social impacts) are considered.\n\t\t\n\t\t\
      - The scope statement specifies which aspects, activities, processes, or entities are included in the evaluation. For\
      \ example, in a greenhouse gas (GHG) emissions assessment, the boundary might cover Scope 1 (direct emissions), Scope\
      \ 2 (indirect emissions from energy use), and Scope 3 (upstream and downstream emissions in the value chain).\n\t\t\n\
      \t\t- The spatial boundaries cover the geographic region(s) relevant for the assessment, including but not limited to\
      \ a specific site, facility, region, or global operations of a company or project.\n\t\t\n\t\t- The relevant timeframe\
      \ may be a single year, the entire lifecycle of a product, or a specific project phase.\n\t\t\n\t\t- Organizational\
      \ boundaries may include a parent company, subsidiaries, joint ventures, or specific divisions based on control, ownership,\
      \ or influence.\n\t\t\n\t\t- Impact may include carbon emissions, energy use, water consumption, biodiversity impact,\
      \ and waste generation.\n\t\t\n\t\t- Lifecycle boundaries may cover product or process evaluations (e.g., Life Cycle\
      \ Assessment or LCA). If so, the boundary defines which stages of the lifecycle are included: Cradle-to-Grave: Includes\
      \ all stages, from raw material extraction to disposal, Cradle-to-Gate: Covers stages up to the point where the product\
      \ leaves the manufacturing facility. or Gate-to-Gate: Focuses on a specific segment of the lifecycle, such as manufacturing\
      \ processes, for example.\n\t\t\n\t\t- Small, immaterial emissions sources might be excluded if their impact is negligible.\n\
      \t\t\n\t\t- Stakeholder boundaries with respect to a given sustainability evaluation might include impacts on local\
      \ communities or supply chain partners."
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/SitesAndFacilities/Site
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/involves
  - filler: https://www.omg.org/spec/Commons/Locations/GeographicRegion
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/hasSpatialBoundary
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/SitesAndFacilities/Facility
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/Context
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Specification
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/AssessmentBoundary
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: assessment boundary
type: Ontology Class
---

# assessment boundary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/AssessmentBoundary>

## Definition

defined scope, limits, and criteria used to determine what is included or excluded in an evaluation, analysis, or measurement of environmental impacts, sustainability performance, or related objectives

## Relationships

- **Subclass of**: [Context](<https://www.omg.org/spec/Commons/ContextualDesignators/Context>)
- **Subclass of**: [Specification](<https://www.omg.org/spec/Commons/Documents/Specification>)

## Constraints

- **[involves](/concepts/fibo/FND/Relations/Relations/involves.md)**: min qualified cardinality 0 of type [Site](<https://www.omg.org/spec/Commons/SitesAndFacilities/Site>)
- **[hasSpatialBoundary](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/hasSpatialBoundary.md)**: some values from of type [GeographicRegion](<https://www.omg.org/spec/Commons/Locations/GeographicRegion>)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: min qualified cardinality 0 of type [Facility](<https://www.omg.org/spec/Commons/SitesAndFacilities/Facility>)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: min qualified cardinality 0 of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: assessment boundary
- **definition**: defined scope, limits, and criteria used to determine what is included or excluded in an evaluation, analysis, or measurement of environmental impacts, sustainability performance, or related objectives
- **explanatoryNote**: The assessment boundary ensures consistency, transparency, and focus by specifying the parameters for the evaluation. It includes: (1) the scope of assessment, (2) the relevant spacial boundaries, (3) the time period(s) over which the assessment is to be conducted, (4) organizational boundaries - which parts of an organization or project are included in the evaluation, (5) impact categories - which environmental or sustainability impacts are included, (6) lifecycle boundaries - which stages of the lifecycle are included, (7) exclusions - specific elements, processes, or impacts that are excluded from the assessment and justification for these exclusions, and (8) stakeholder boundaries - the extent to which external stakeholders or externalities (e.g., indirect social impacts) are considered. 		 		- The scope statement specifies which aspects, activities, processes, or entities are included in the evaluation. For example, in a greenhouse gas (GHG) emissions assessment, the boundary might cover Scope 1 (direct emissions), Scope 2 (indirect emissions from energy use), and Scope 3 (upstream and downstream emissions in the value chain). 		 		- The spatial boundaries cover the geographic region(s) relevant for the assessment, including but not limited to a specific site, facility, region, or global operations of a company or project. 		 		- The relevant timeframe may be a single year, the entire lifecycle of a product, or a specific project phase. 		 		- Organizational boundaries may include a parent company, subsidiaries, joint ventures, or specific divisions based on control, ownership, or influence. 		 		- Impact may include carbon emissions, energy use, water consumption, biodiversity impact, and waste generation. 		 		- Lifecycle boundaries may cover product or process evaluations (e.g., Life Cycle Assessment or LCA). If so, the boundary defines which stages of the lifecycle are included: Cradle-to-Grave: Includes all stages, from raw material extraction to disposal, Cradle-to-Gate: Covers stages up to the point where the product leaves the manufacturing facility. or Gate-to-Gate: Focuses on a specific segment of the lifecycle, such as manufacturing processes, for example. 		 		- Small, immaterial emissions sources might be excluded if their impact is negligible. 		 		- Stakeholder boundaries with respect to a given sustainability evaluation might include impacts on local communities or supply chain partners.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

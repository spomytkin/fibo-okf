---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: municipal security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt obligation issued by a regional governmental entity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A municipal security is typically a bond, note, warrant, certificate or other similar obligation issued by a state
      or local government or their agencies or authorities (such as cities, towns, villages, counties or special districts
      or authorities). A prime feature of most municipal securities is that interest or other investment earnings on them
      are generally excluded from gross income of the bondholder for federal income tax purposes. Some municipal securities
      are subject to federal income tax, although the issuers or bondholders may receive other federal tax advantages for
      certain types of taxable municipal securities. Some examples include Build America Bonds, municipal fund securities
      and direct pay subsidy bonds.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/SovereignDebtInstrument.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignDebtInstrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalDebtFundsUsage
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: N746ac9eb82574356b49169065302564b
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalDebtSourceOfFunds
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFundingSource
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalSecurity
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: municipal security
type: Ontology Class
---

# municipal security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalSecurity>

## Definition

debt obligation issued by a regional governmental entity

## Relationships

- **Subclass of**: [GovernmentIssuedDebtSecurity](/concepts/fibo/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity.md)

## Constraints

- **Disjoint with**: [SovereignDebtInstrument](/concepts/fibo/SEC/Debt/Bonds/SovereignDebtInstrument.md)
- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: some values from of type [MunicipalDebtFundsUsage](/concepts/fibo/SEC/Debt/Bonds/MunicipalDebtFundsUsage.md)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from value `N746ac9eb82574356b49169065302564b`
- **[hasFundingSource](/concepts/fibo/SEC/Debt/Bonds/hasFundingSource.md)**: some values from of type [MunicipalDebtSourceOfFunds](/concepts/fibo/SEC/Debt/Bonds/MunicipalDebtSourceOfFunds.md)

## Annotations

- **label**: municipal security
- **definition**: debt obligation issued by a regional governmental entity
- **explanatoryNote**: A municipal security is typically a bond, note, warrant, certificate or other similar obligation issued by a state or local government or their agencies or authorities (such as cities, towns, villages, counties or special districts or authorities). A prime feature of most municipal securities is that interest or other investment earnings on them are generally excluded from gross income of the bondholder for federal income tax purposes. Some municipal securities are subject to federal income tax, although the issuers or bondholders may receive other federal tax advantages for certain types of taxable municipal securities. Some examples include Build America Bonds, municipal fund securities and direct pay subsidy bonds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

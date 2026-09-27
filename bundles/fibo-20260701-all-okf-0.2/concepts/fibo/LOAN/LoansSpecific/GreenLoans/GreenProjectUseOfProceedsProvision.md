---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: Loan Market Association (LMA) Green Loan Principles, available at https://www.icmagroup.org/assets/documents/Regulatory/Green-Bonds/LMA_Green_Loan_Principles_Booklet-220318.pdf.
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: green project use of proceeds provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: use of proceeds provision specifying that funds obtained through financing, such as through a credit agreement,
      offering, warrant, or other instrument are intended to be used for Green Projects (including other related and supporting
      expenditures, including research and development)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "All designated Green Projects should provide clear environmental benefits, which will be assessed, and where feasible,\
      \ quantified, measured and reported by the borrower, per requirements outlined in the LMA Green Loan Principles (GLP).\
      \ Where funds are to be used, in whole or part, for refinancing, it is recommended that borrowers provide an estimate\
      \ of the share of financing versus refinancing. Where appropriate, they should also clarify which investments or project\
      \ portfolios may be refinanced, and, to the extent relevant, the expected look-back period for refinanced Green Projects.\
      \ A green loan may take the form of one or more tranches of a loan facility. In such cases, the green tranche(s) must\
      \ be clearly designated, with proceeds of the green tranche(s) credited to a separate account or tracked by the borrower\
      \ in an appropriate manner. \n\t\t\n\t\tThe GLP explicitly recognise several broad categories of eligibility for Green\
      \ Projects with the objective of addressing key areas of environmental concern such as climate change, natural resources\
      \ depletion, loss of biodiversity, and air, water and soil pollution. This non-exhaustive list, set out in Appendix\
      \ 1, is intended to capture the most usual types of projects supported, and expected to be supported, by the green loan\
      \ market. However, it is recognised that definitions of green and green projects may vary depending on sector and geography"
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenProject
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/UseOfProceedsProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/UseOfProceedsProvision
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenProjectUseOfProceedsProvision
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: green project use of proceeds provision
type: Ontology Class
---

# green project use of proceeds provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenProjectUseOfProceedsProvision>

## Definition

use of proceeds provision specifying that funds obtained through financing, such as through a credit agreement, offering, warrant, or other instrument are intended to be used for Green Projects (including other related and supporting expenditures, including research and development)

## Relationships

- **Subclass of**: [UseOfProceedsProvision](/concepts/fibo/FND/Agreements/Contracts/UseOfProceedsProvision.md)

## Constraints

- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [GreenProject](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/GreenProject.md)

## Annotations

- **source**: Loan Market Association (LMA) Green Loan Principles, available at https://www.icmagroup.org/assets/documents/Regulatory/Green-Bonds/LMA_Green_Loan_Principles_Booklet-220318.pdf.
- **label**: green project use of proceeds provision
- **definition**: use of proceeds provision specifying that funds obtained through financing, such as through a credit agreement, offering, warrant, or other instrument are intended to be used for Green Projects (including other related and supporting expenditures, including research and development)
- **explanatoryNote**: All designated Green Projects should provide clear environmental benefits, which will be assessed, and where feasible, quantified, measured and reported by the borrower, per requirements outlined in the LMA Green Loan Principles (GLP). Where funds are to be used, in whole or part, for refinancing, it is recommended that borrowers provide an estimate of the share of financing versus refinancing. Where appropriate, they should also clarify which investments or project portfolios may be refinanced, and, to the extent relevant, the expected look-back period for refinanced Green Projects. A green loan may take the form of one or more tranches of a loan facility. In such cases, the green tranche(s) must be clearly designated, with proceeds of the green tranche(s) credited to a separate account or tracked by the borrower in an appropriate manner.  		 		The GLP explicitly recognise several broad categories of eligibility for Green Projects with the objective of addressing key areas of environmental concern such as climate change, natural resources depletion, loss of biodiversity, and air, water and soil pollution. This non-exhaustive list, set out in Appendix 1, is intended to capture the most usual types of projects supported, and expected to be supported, by the green loan market. However, it is recognised that definitions of green and green projects may vary depending on sector and geography

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
